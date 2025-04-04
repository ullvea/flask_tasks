import asyncio
import os
import time

REST_TIME = 5
COEFF = 100


async def do_work(name, time_to_do_task1, time_to_prepare1,
                  time_to_do_task2, time_to_prepare2):
    time_to_do_task1, time_to_prepare1, time_to_do_task2, time_to_prepare2 = (
        time_to_do_task1 / COEFF, time_to_prepare1 / COEFF, time_to_do_task2 / COEFF, time_to_prepare2 / COEFF)
    print(f'{name} started the 1 task')
    await asyncio.sleep(time_to_do_task1)
    print(f"{name} moved on to the defense of the 1 task.")
    await asyncio.sleep(time_to_prepare1)
    print(f'{name} completed the 1 task')
    print(f'{name} is resting')
    await asyncio.sleep(REST_TIME)

    print(f'{name} started the 2 task')
    await asyncio.sleep(time_to_do_task2)
    print(f"{name} moved on to the defense of the 2 task.")
    await asyncio.sleep(time_to_prepare2)
    print(f'{name} completed the 2 task')


async def interviews(*params):
    timetable = []
    for i in params:
        timetable.append(asyncio.create_task(do_work(*i)))
    await asyncio.gather(*timetable)


if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
t0 = time.time()
asyncio.run(interviews(*data))
print(time.time() - t0)
