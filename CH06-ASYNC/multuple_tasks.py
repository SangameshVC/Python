import asyncio
import time

async def api_call(url,delay=10):
    print("Fetching data from",url)
    await asyncio.sleep(delay)             #resources are released
    print("Data fetched from",url)
    
async def execution():                   #resources are not relesed
    time.sleep(5)
    print("Execution completed")
    
async def transformation():
    await asyncio.sleep(2)                   #resources are released
    print("Transformation completed")
    
async def main():
    
    tasks=await asyncio.gather(
        api_call("url"),           #we are not passing delay bcz it's hardcoded in function only
        execution(),
        transformation()
    )
    
    print("All tasks are completed")
    
asyncio.run(main())


"""  O/P
Fetching data from url
Execution completed
Transformation completed
Data fetched from url
All tasks are completed

Here frst it calls api_call(), then resources are released. SO it moves to execution() function, resources are hold for 5 seconds.
It waits there for 5 seconds to complete that task bcz we mentioned(time.sleep()).Once execution() completed it moves to transformation.
Here frst it completes transformation bcz api_call takes 10 seconds so again it moves to transformation()."""