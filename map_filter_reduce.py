# The Lambda function is an anonymous functions. They can have any number of arguments but only one expression. Lambda functions are often used for short, simple operations,

""" 
add = lambda x, y: x + y
print(add(10,20)) 
"""
"""
# Using a lambda function within another function
def make_incrementor(n):
    return lambda x: x + n

increment_by_5 = make_incrementor(5)
print(increment_by_5(10)) # 15
"""

"""
min_value = lambda x, y: x if x < y else y
print(min_value(10, 20))  # 10
"""

# The map function applies a given function to all items in an input iterable (such as a list or tuple) and returns an iterator that yields the results.

""" 
# Squaring a number
n = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, n)
result_list = list(squared_numbers)
print(result_list)
# Output: [1, 4, 9, 16, 25] 
"""

""" 
# Captilizing the words
words = ['apple', 'banana', 'cherry']
capitalized_words = map(str.capitalize, words)
result_list = list(capitalized_words)
print(result_list)
# Output: ['Apple', 'Banana', 'Cherry'] 
"""

# The filter function in Python is used to construct an iterator from elements of an iterable for which a function returns true.

""" 
# Filtering Odd Numbers
n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_numbers = filter(lambda x: x % 2 != 0, n)
result_list = list(filtered_numbers)
print(result_list)
# Output: [1, 3, 5, 7, 9]
"""

""" 
# Removing None Values from a List
values = [1, None, 3, None, 5, None, 7]
filtered_values = filter(lambda x: x is not None, values)
result_list = list(filtered_values)
print(result_list)
# Output: [1, 3, 5, 7]
"""

#  The reduce function is used to apply a function to an iterable to cumulatively reduce it to a single value.

""" 
# Summing a List of Numbers
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)
# Output: 15
"""

""" 
# Factorial Calculation
from functools import reduce

n = 5
factorial_result = reduce(lambda x, y: x * y, range(1, n+1), 1)
print(factorial_result)
# Output: 120
"""

# The strip() method removes any leading and trailing whitespace characters (spaces, newlines, tabs) from a string.
""" 
text = "  Hello, World!  "
clean_text = text.strip()
print(f"'{clean_text}'")  # 'Hello, World!'

text = "--Hi Man --"
clean_text = text.strip("-")
print(f"{clean_text}") # Hi Man
"""

# The split() method divides a string into a list of substrings based on a specified delimiter.
""" 
text = "Hello World Python"
words = text.split()
print(words)  # ['Hello', 'World', 'Python']

text = "one two three four"
parts = text.split(' ', 2)
print(parts)  # ['one', 'two', 'three four']
"""

""" 
text = "   apple, banana, cherry   "
fruits = text.strip().split(",",1)
print(fruits) # ['apple', ' banana, cherry'] 
"""