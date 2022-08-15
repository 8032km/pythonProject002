import threading
import time
from time import sleep

"""x = []


def cook(name='bludo', t=3):
    print(f"You started cooking {name}")
    sleep(t)
    print(f'{name} ready')"""

"""t1 = threading.Thread(target=cook, args=('borsch',))
t2 = threading.Thread(target=cook, args=('rise',))
t3 = threading.Thread(target=cook, args=('plov',))

t1.start()
t2.start()

t2.join()
print('U can use for plov')
t3.start()

t1.join()
t3.join()"""

"""def func():
    for i in range(1000000):
        pass


def func2():
    time1 = time.time()
    t1 = threading.Thread(target=func)
    t2 = threading.Thread(target=func)
    t3 = threading.Thread(target=func)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print(time.time() - time1)


func2()"""
import asyncio

"""
# baza

async def cook(name='bludo', t=3):
    print(f"You started cooking {name}")
    await asyncio.sleep(t)
    print(f'{name} ready')


async def main():
    x = await cook('cock')
    await cook('balls')


loop = asyncio.get_event_loop()"""

"""tasks = asyncio.gather(cook('cock'), cook('balls'))"""

"""loop.run_until_complete(main())"""

import time


async def main():
    for i in range(10):
        print(i)
        await asyncio.sleep(1)


print(main)


async def func():
    task1 = asyncio.create_task(main())
    task2 = asyncio.create_task(main())
    task3 = asyncio.create_task(main())
    await task1
    await task2
    await task3

loop = asyncio.get_event_loop()
loop.run_until_complete(func())
