import asyncio
import os
import time

REST_TIME = 5
COEFF = 100


async def do_work(name, time_to_do_task1, time_to_prepare1,
                  time_to_do_task2, time_to_prepare2):
    time_to_do_task1, time_to_prepare1, time_to_do_task2, time_to_prepare2 = (
        time_to_do_task1 / COEFF, time_to_prepare1 / COEFF, time_to_do_task2 / COEFF, time_to_prepare2 / COEFF)
    print(f'{name} started the 1 task.')
    await asyncio.sleep(time_to_do_task1)
    print(f"{name} moved on to the defense of the 1 task.")
    await asyncio.sleep(time_to_prepare1)
    print(f'{name} completed the 1 task.')

    print(f'{name} started the 2 task.')
    await asyncio.sleep(time_to_do_task2)
    print(f"{name} moved on to the defense of the 2 task.")
    await asyncio.sleep(time_to_prepare2)
    print(f'{name} completed the 2 task.')


async def interviews_2(*params):
    timetable = []
    for i in params:
        timetable.append(asyncio.create_task(do_work(*i)))
    await asyncio.gather(*timetable)


if __name__ == '__main__':
    t0 = time.time()  # запоминаем время начала работы
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
