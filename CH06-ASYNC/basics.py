import asyncio
import time

# Coroutine function
async def main():       #coroutine functions starts with async
    print("Hello") # This will print immediately
    await asyncio.sleep(3) # we mentioned await here bcz to complete this task before jumping to next step
    print("World") # This will be executed right after the first statement if we won't mention await

# Run the main coroutine
asyncio.run(main())