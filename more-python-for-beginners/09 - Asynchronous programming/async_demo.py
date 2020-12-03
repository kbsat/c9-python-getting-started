from timeit import default_timer
import aiohttp
import asyncio

async def load_data(session, delay):
    print(f'Starting {delay} second timer')
    async with session.get(f'http://httpbin.org/delay/{delay}') as resp:
        text = await resp.text()
        print(f'Completed {delay} second timer')
        return text

async def main():
    # 타이머 동작하기
    start_time = default_timer()

    # 단일 세션 생성하기
    async with aiohttp.ClientSession() as session:
        # 작업 생성하고 실행하기
        two_task = asyncio.create_task(load_data(session, 2))
        three_task = asyncio.create_task(load_data(session, 3))

        # 다른 처리 시뮬레이션
        await asyncio.sleep(1)
        print('Doing other work')

        # 우리의 값을 얻어보자
        two_result = await two_task
        three_result = await three_task

        # 결과 값 출력
        elapsed_time = default_timer() - start_time
        print(f'The operation took {elapsed_time:.2} seconds')

asyncio.run(main())
