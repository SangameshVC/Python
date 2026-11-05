#Normal sync API calls

import time

def api_call():
    time.sleep(3)                   #Thread is locked
    return "Orders data"

def execute():
    print("Executing API Call")
    result=api_call()
    print("Data Fetched", result)
    
execute()

#-------------------------------------------------------
#Async API calls
import asyncio

async def api_call():
    await asyncio.sleep(3)             #thread is released and here we mentioned await to wait for function to complete
    return("Orders Data")
    
async def execute():
    print("Executing API Call")
    result = await api_call()                #waits till it get result from function,after it prints next statement
    print("Data Fetched:",result)

asyncio.run(execute())


#And make sure to call async functions inside async functions. DOn't call sync functions inside async