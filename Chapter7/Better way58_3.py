from queue import Queue
from threading import Thread
from threading import Lock
import time

from queue import Queue

class ClosableQueue(Queue):
    SENTINEL = object()

    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return   # 스레드를 종료시킨다
                yield item
            finally:
                self.task_done()

in_queue = ClosableQueue()
logic_queue = ClosableQueue()
out_queue = ClosableQueue()

class StoppableWorker(Thread):
    def __init__(self, func, in_queue, out_queue, **kwargs):
        super().__init__(**kwargs)
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)

ALIVE = '*'
EMPTY = '-'

class SimulationError(Exception):
    pass

class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)

    def get(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def set(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state

    def __str__(self):
        output = ''
        for row in self.rows:
            for cell in row:
                output += cell
            output += '\n'
        return output

class LockingGrid(Grid):
    def __init__(self, height, width):
        super().__init__(height, width)
        self.lock = Lock()

    def __str__(self):
        with self.lock:
            return super().__str__()

    def get(self, y, x):
        with self.lock:
            return super().get(y, x)

    def set(self, y, x, state):
        with self.lock:
            return super().set(y, x, state)

def count_neighbors(y, x, get):
    n_ = get(y - 1, x + 0) # 북(N)
    ne = get(y - 1, x + 1) # 북동(NE)
    e_ = get(y + 0, x + 1) # 동(E)
    se = get(y + 1, x + 1) # 남동(SE)
    s_ = get(y + 1, x + 0) # 남(S)
    sw = get(y + 1, x - 1) # 남서(SW)
    w_ = get(y + 0, x - 1) # 서(W)
    nw = get(y - 1, x - 1) # 북서(NW)
    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    # 여기서 블러킹 I/O를 수행한다
    #data = my_socket.recv(100)
    return count

def count_neighbors_thread(item):
    y, x, state, get = item
    try:
        neighbors = count_neighbors(y, x, get)
    except Exception as e:
        neighbors = e
    return (y, x, state, neighbors)

def game_logic(state, neighbors):
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY # 살아 있는 이웃이 너무 적음: 죽음
        elif neighbors > 3:
            return EMPTY # 살아 있는 이웃이 너무 많음: 죽음
    else:
        if neighbors == 3:
            return ALIVE # 다시 생성됨

    # 여기서 블러킹 I/O를 수행한다
    #data = my_socket.recv(100)
    return state

def game_logic_thread(item):
    y, x, state, neighbors = item
    try:
        next_state = game_logic(state, neighbors)
    except Exception as e:
        next_state = e
    return (y, x, next_state)

# 스레드를 미리 시작한다
threads = []

for _ in range(5):
    thread = StoppableWorker(
        count_neighbors_thread, in_queue, logic_queue)
    thread.start()
    threads.append(thread)

for _ in range(5):
    thread = StoppableWorker(
        game_logic_thread, logic_queue, out_queue)
    thread.start()
    threads.append(thread)

def step_cell(y, x, get, set):
    state = get(y, x)
    neighbors = count_neighbors(y, x, get)
    next_state = game_logic(state, neighbors)
    set(y, x, next_state)

class ColumnPrinter:
    def __init__(self):
        self.columns = []

    def append(self, data):
        self.columns.append(data)

    def __str__(self):
        row_count = 1
        for data in self.columns:
            row_count = max(
                row_count, len(data.splitlines()) + 1)

        rows = [''] * row_count
        for j in range(row_count):
            for i, data in enumerate(self.columns):
                line = data.splitlines()[max(0, j - 1)]
                if j == 0:
                    padding = ' ' * (len(line) // 2)
                    rows[j] += padding + str(i) + padding
                else:
                    rows[j] += line

                if (i + 1) < len(self.columns):
                    rows[j] += ' | '

        return '\n'.join(rows)


def simulate_phased_pipeline(
        grid, in_queue, logic_queue, out_queue):
    for y in range(grid.height):
        for x in range(grid.width):
            state = grid.get(y, x)
            item = (y, x, state, grid.get)
            in_queue.put(item)  # 팬아웃

    in_queue.join()
    logic_queue.join()  # 파이프라인을 순서대로 실행한다
    out_queue.close()

    next_grid = LockingGrid(grid.height, grid.width)
    for item in out_queue:  # 팬인
        y, x, next_state = item
        if isinstance(next_state, Exception):
            raise SimulationError(y, x) from next_state
        next_grid.set(y, x, next_state)
    return next_grid

grid = Grid(5, 9)
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)

columns = ColumnPrinter()
for i in range(5):
    columns.append(str(grid))
    grid = simulate_phased_pipeline(
        grid, in_queue, logic_queue, out_queue)

print(columns)

for thread in threads:
    in_queue.close()
for thread in threads:
    logic_queue.close()
for thread in threads:
    thread.join()
