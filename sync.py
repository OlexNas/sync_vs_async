import datetime
import colorama
import random
import time
import asyncio


def main():

    loop = asyncio.get_event_loop()
    t0 = datetime.datetime.now() # Declare start time
    print(colorama.Fore.WHITE + "App started.", flush=True)
    data = [] # Declare list
    generate_data(10, data)
    generate_data(10, data)
    process_data(20, data)

    dt = datetime.datetime.now() - t0
    print(colorama.Fore.WHITE + "App exiting, total time: {:,.2f} sec.".format(dt.total_seconds()), flush=True)


def generate_data(num: int, data: list):
    for idx in range(1, num + 1):
        item = idx*idx
        createTuple = (item, datetime.datetime.now())
        data.append(createTuple)

        print(colorama.Fore.YELLOW + " -- generated item {}".format(idx), flush=True)
        time.sleep(random.random() + .5)


def process_data(num: int, data: list):
    processed = 0
    while processed < num:
        item = data.pop(0)
        if not item:
            time.sleep(.01)
            continue

        processed += 1
        value = item[0]
        t = item[1]
        dt = datetime.datetime.now() - t

        print(colorama.Fore.CYAN +
              " +++ Processed value {} after {:,.2f} sec.".format(value, dt.total_seconds()), flush=True)
        time.sleep(.5)


if __name__ == '__main__':
    main()