# import asyncio
# import time
# import aiohttp
#
#
# @asyncio.coroutine
# def download_site(session, url):
#     response = yield session.get(url)
#     print("Read {0} from {1}".format(response.content_length, url))
#
# @asyncio.coroutine
# def download_all_sites(sites):
#     session = aiohttp.ClientSession()
#
#     tasks = []
#     for url in sites:
#
#         x = yield download_site(session, url)
#         print (x)
#         # task = asyncio.ensure_future(download_site(session, url))
#         # tasks.append(task)
#
#     #    yield asyncio.gather(*tasks, return_exceptions=True)
#     yield session.close()
#
#
# if __name__ == "__main__":
#     sites = [
#                 "https://www.jython.org",
#                 "http://olympus.realpython.org/dice",
#             ] * 80
#     start_time = time.time()
#     # asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
#
#     # use this only when in jupyter notebook (Jupyter is running already on asyncio
#     # so an event loop is already present)
#     coro = download_all_sites(sites)
#     asyncio.get_event_loop().create_task(coro)
#
#     duration = time.time() - start_time
#     print(f"Downloaded {len(sites)} sites in {duration} seconds")

import asyncio
import time
import aiohttp


@asyncio.coroutine
def download_site(session, url):
    response = yield from session.get(url)
    print("Read {0} from {1}".format(response.content_length, url))

@asyncio.coroutine
def sleep():
    # time.sleep(.5)
    return 2

@asyncio.coroutine
def download_all_sites(sites):
    session = aiohttp.ClientSession()

    try:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)

        yield from sleep()
        yield from asyncio.gather(*tasks, return_exceptions=True)
    finally:
        yield from session.close()


if __name__ == "__main__":
    sites = [
                "https://www.jython.org",
                "http://olympus.realpython.org/dice",
            ] * 80
    start_time = time.time()
    # asyncio.get_event_loop().run_until_complete(download_all_sites(sites))

    # use this only when in jupyter notebook (Jupyter is running already on asyncio
    # so an event loop is already present)
    coro = download_all_sites(sites)
    asyncio.get_event_loop().run_until_complete(coro)

    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")
