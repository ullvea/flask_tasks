import asyncio
import os
import time
import sys

REST_TIME = 5
COEFF = 100
gifts = dict()


async def printf(item, chose, prep):
    await asyncio.sleep(chose)
    print(f'Buy {item}')
    await asyncio.sleep(prep)
    print(f'Got {item}')


async def do_work(to_start_time, duration, num):
    print(f'Buying gifts at {num} shop')
    time.sleep(to_start_time)
    time.sleep(duration)
    gift_to_buy = None
    for item, value in gifts.items():
        if sum(value) <= duration:
            gift_to_buy = [item, value[0], value[1]]
            asyncio.create_task(*gift_to_buy)
    print(f'Arrive from {num} stop')


async def shopping(shops):
    timetable = []
    num = 1
    for i in shops:
        timetable.append(asyncio.create_task(do_work(*i, num)))
        num += 1
    await asyncio.gather(*timetable)


if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    data = [i.strip('\n') for i in sys.stdin]
    # print(data)
    shops, gifts = [], dict()
    flag = False
    for i in data:
        if i != '' and not flag:
            a, b = i.split()
            shops.append([int(a) / COEFF, int(b) / COEFF])
        elif i == '':
            flag = True
        elif flag:
            gift_name, a, b = i.split()
            gifts[gift_name] = [int(a) / COEFF, int(b) / COEFF]
    gifts = dict(sorted(gifts.items(), key=lambda item: item[1], reverse=True))
    asyncio.run(shopping(shops))
    if len(gifts.keys()) != 0:
        print('Buying gifts after arrival')
