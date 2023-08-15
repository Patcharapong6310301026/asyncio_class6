#1-1-hello-world-wrong.py
#When do corotuines start running?
import asyncio
import time

async def print_after(message, delay):
    """Print a message after the specified delay (in seconds)"""
    await asyncio.sleep(delay)
    print(f"{time.ctime()} - {message}")
    
async def main():
    # Start corotine twice (hopefully they start!)
    first_awaitable = print_after("world!", 2)
    second_awaitable = print_after("Hello", 1)
    # Wait for corotines to finish
    await first_awaitable
    await second_awaitable
    
asyncio.run(main())