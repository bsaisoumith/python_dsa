# Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object. enumerate(iterable, start=0)


import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end-start)*1000) + " mil sec ")
        return result
    return wrapper

@time_it
def linear_search(numbers_list, numbers_to_find):
    for index, element in enumerate(numbers_list):
        if element == numbers_to_find:
            return index
    return -1

@time_it
def binary_search(numbers_list, numbers_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == numbers_to_find:
            return mid_index
        
        if mid_number < numbers_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1

@time_it
def binary_search_recursive(numbers_list, numbers_to_find, left_index, right_index):
    if right_index < left_index:
        return -1
    
    mid_index = (left_index + right_index) // 2
    mid_number = numbers_list[mid_index]

    if mid_number == numbers_to_find:
        return mid_index
    
    if mid_number < numbers_to_find:
            left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, numbers_to_find, left_index, right_index)

if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    numbers_to_find = 45

    """ numbers_list = [i for i in range(1000000)]
    numbers_to_find = 100000 """

    index = linear_search(numbers_list, numbers_to_find)
    print(f"Number found at index {index} using Linear search")

    index = binary_search(numbers_list,numbers_to_find)
    print(f"Number found at index {index} using Binary search")

    index = binary_search_recursive(numbers_list, numbers_to_find, 0, len(numbers_list) - 1)
    print(f"Number found at index {index} using Binary search recursive")