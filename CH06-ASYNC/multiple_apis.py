import asyncio

async def api_call(url,delay):
    print("Fetching data from ",url)
    await asyncio.sleep(delay)
    print("Data fetched from ",url)
    return f"{url} data"

async def main():
    tasks = await asyncio.gather(
        api_call("url1",3),
        api_call("url2",2),
        api_call("url3",1)
    )
    
    #Another way to create tasks with list comprehension
    # tasks = [api_call(url, delay) for url, delay in [("https://api1.com", 2), ("https://api2.com", 3), ("https://api3.com", 1)]]
    # results = await asyncio.gather(*tasks)
    
    print("All tasks are completed")
    print(tasks)
    
asyncio.run(main())