# A callback function in Python is a function that is passed as an argument to another function and is executed when some event occurs.

""" 
def callback_function(message):
    print(f"Callback received: {message}")

def main_function(callback):
    # Do some work
    result = "Operation completed successfully"
    
    # Invoke the callback function
    callback(result)

# Example usage
main_function(callback_function)
"""

import asyncio

async def async_callback_function(message):
    print(f"Async Callback received: {message}")

async def async_main_function(callback):
    # Simulate some asynchronous work
    await asyncio.sleep(2)
    
    # Invoke the async callback function
    await callback("Async operation completed successfully")

# Example usage
asyncio.run(async_main_function(async_callback_function))