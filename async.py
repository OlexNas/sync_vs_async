import datetime
from asyncio import AbstractEventLoop

import colorama
import random
import time
import asyncio


def main():

    loop: AbstractEventLoop = asyncio.get_event_loop()
    t0 = datetime.datetime.now() # Declare start time
    print(colorama.Fore.WHITE + "App started.", flush=True)
    data = asyncio.Queue()

    # generate_data(10, data)
    # generate_data(10, data)
    # process_data(20, data)

    task = asyncio.gather(
        generate_data(10, data),
        generate_data(10, data),
        process_data(20, data)
        )

    loop.run_until_complete(task)

    dt = datetime.datetime.now() - t0
    print(colorama.Fore.WHITE + "App exiting, total time: {:,.2f} sec.".format(dt.total_seconds()), flush=True)


async def generate_data(num: int, data: asyncio.Queue):
    for idx in range(1, num + 1):
        item = idx*idx
        work = (item, datetime.datetime.now())
        # data.append(createTuple)
        await data.put(work)

        print(colorama.Fore.YELLOW + " -- generated item {}".format(idx), flush=True)
        await asyncio.sleep(random.random() + .5)


async def process_data(num: int, data: asyncio.Queue):
    processed = 0
    while processed < num:
        # item = data.pop(0)
        # if not item:
        #     time.sleep(.01)
        #     continue

        item = await data.get()  # item is a tuple

        processed += 1
        value = item[0]
        t = item[1]
        dt = datetime.datetime.now() - t

        print(colorama.Fore.CYAN +
              " +++ Processed value {} after {:,.2f} sec.".format(value, dt.total_seconds()), flush=True)
        await asyncio.sleep(.5)


if __name__ == '__main__':
    main()