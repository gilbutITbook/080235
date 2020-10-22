# python 3.8 이상에서만 실행됨(walus연산자때문)

class EOFError(Exception):
    pass


class AsyncConnectionBase:
    def __init__(self, reader, writer):  # 변경됨
        self.reader = reader  # 변경됨
        self.writer = writer  # 변경됨

    async def send(self, command):
        line = command + '\n'
        data = line.encode()
        self.writer.write(data)  # 변경됨
        await self.writer.drain()  # 변경됨

    async def receive(self):
        line = await self.reader.readline()  # 변경됨
        if not line:
            raise EOFError('연결 닫힘')
        return line[:-1].decode()

import random

WARMER = '더따뜻함'
COLDER = '더차가움'
UNSURE = '잘모르겠음'
CORRECT = '맞음'

class UnknownCommandError(Exception):
    pass

class AsyncSession(AsyncConnectionBase):  # 변경됨
    def __init__(self, *args):
        super().__init__(*args)
        self._clear_state(None, None)

    def _clear_state(self, lower, upper):
        self.lower = lower
        self.upper = upper
        self.secret = None
        self.guesses = []

    async def loop(self):  # 변경됨
        while command := await self.receive():  # 변경됨
            parts = command.split(' ')
            if parts[0] == 'PARAMS':
                self.set_params(parts)
            elif parts[0] == 'NUMBER':
                await self.send_number()  # 변경됨
            elif parts[0] == 'REPORT':
                self.receive_report(parts)
            else:
                raise UnknownCommandError(command)

    def set_params(self, parts):
        assert len(parts) == 3
        lower = int(parts[1])
        upper = int(parts[2])
        self._clear_state(lower, upper)

    def next_guess(self):
        if self.secret is not None:
            return self.secret

        while True:
            guess = random.randint(self.lower, self.upper)
            if guess not in self.guesses:
                return guess

    async def send_number(self):
        guess = self.next_guess()
        self.guesses.append(guess)
        await self.send(format(guess))

    def receive_report(self, parts):
        assert len(parts) == 2
        decision = parts[1]
        last = self.guesses[-1]
        if decision == CORRECT:
            self.secret = last

        print(f'서버: {last}는 {decision}')


import contextlib
import math

class AsyncClient(AsyncConnectionBase):
    def __init__(self, *args):
        super().__init__(*args)
        self._clear_state()

    def _clear_state(self):
        self.secret = None
        self.last_distance = None

    @contextlib.asynccontextmanager                         # 변경됨
    async def session(self, lower, upper, secret):          # 변경됨
        print(f'\n{lower}와 {upper} 사이의 숫자를 맞춰보세요!'
              f' 쉿! 그 숫자는 {secret} 입니다.')
        self.secret = secret
        await self.send(f'PARAMS {lower} {upper}')          # 변경됨
        try:
            yield
        finally:
            self._clear_state()
            await self.send('PARAMS 0 -1')                   # 변경됨

    async def request_numbers(self, count):            # 변경됨
        for _ in range(count):
            await self.send('NUMBER')                  # 변경됨
            data = await self.receive()                # 변경됨
            yield int(data)
            if self.last_distance == 0:
                return

    async def report_outcome(self, number):                    # 변경됨
        new_distance = math.fabs(number - self.secret)
        decision = UNSURE

        if new_distance == 0:
            decision = CORRECT
        elif self.last_distance is None:
            pass
        elif new_distance < self.last_distance:
            decision = WARMER
        elif new_distance > self.last_distance:
            decision = COLDER

        self.last_distance = new_distance

        await self.send(f'REPORT {decision}')                  # 변경됨

        # 잠시 대기해서 출력 순서 조정
        await asyncio.sleep(0.01)
        return decision

import asyncio

async def handle_async_connection(reader, writer):
    session = AsyncSession(reader, writer)
    try:
        await session.loop()
    except EOFError:
        pass

async def run_async_server(address):
    server = await asyncio.start_server(
        handle_async_connection, *address)
    async with server:
        await server.serve_forever()

async def run_async_client(address):
    # 서버가 시작될 수 있게 기다려주기
    await asyncio.sleep(0.1)

    streams = await asyncio.open_connection(*address)   # New
    client = AsyncClient(*streams)                      # New

    async with client.session(1, 5, 3):
        results = [(x, await client.report_outcome(x))
                   async for x in client.request_numbers(5)]

    async with client.session(10, 15, 12):
        async for number in client.request_numbers(5):
            outcome = await client.report_outcome(number)
            results.append((number, outcome))

    _, writer = streams                                # 새 기능
    writer.close()                                     # 새 기능
    await writer.wait_closed()                         # 새 기능

    return results

async def main_async():
    address = ('127.0.0.1', 4321)

    server = run_async_server(address)
    asyncio.create_task(server)

    results = await run_async_client(address)
    for number, outcome in results:
        print(f'클라이언트: {number}는 {outcome}')

asyncio.run(main_async())

