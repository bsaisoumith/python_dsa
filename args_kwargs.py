'''
*args and **kwargs are used to pass a variable number of arguments to a function.
*args is used to pass a variable number of non-keyword arguments to a function
**kwargs is used to pass a variable number of keyword arguments to a function
'''

def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3)  
# 1 
# 2 
# 3 



def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(name="John", age=25, location="New York")
# name: John
# age: 25
# location: New York



def my_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

my_function(1, 2, 3, name="John", age=25)
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'John', 'age': 25}



def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper executed this before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display_info(name, age):
    print(f"display_info ran with arguments ({name}, {age})")

display_info('John', 25)

# Wrapper executed this before display_info
# display_info ran with arguments (John, 25)
