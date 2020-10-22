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
    return count

def game_logic(state, neighbors):
    # OSError 발생 에뮬레이션
    raise OSError('게임 로직에서 I/O 문제 발생')

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
        game_logic_thread, in_queue, out_queue)
    thread.start()
    threads.append(thread)

def step_cell(y, x, get, set):
    state = get(y, x)
    neighbors = count_neighbors(y, x, get)
    next_state = game_logic(state, neighbors)
    set(y, x, next_state)

def simulate_pipeline(grid, in_queue, out_queue):
    for y in range(grid.height):
        for x in range(grid.width):
            state = grid.get(y, x)
            neighbors = count_neighbors(y, x, grid.get)
            in_queue.put((y, x, state, neighbors))  # 팬아웃
    in_queue.join()
    out_queue.close()
    next_grid = Grid(grid.height, grid.width)
    for item in out_queue:  # 팬인
        y, x, next_state = item
        if isinstance(next_state, Exception):
            raise SimulationError(y, x) from next_state
        next_grid.set(y, x, next_state)

    return next_grid

simulate_pipeline(Grid(1, 1), in_queue, out_queue)