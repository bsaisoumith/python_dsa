# Odd n even numbers
""" 
max = int(input("Enter max number: "))
odd_numbers = []

for i in range(1, max):
    if i % 2 == 1:
        odd_numbers.append(i)

print("odd Numbers: ", odd_numbers) 
"""

# reversing an array
""" 
def reverse(arr1):
    arr = list(arr1)
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    arr = "".join(arr)
    print(arr)

reverse("Hello")
"""

""" 
# Find duplicate values in an array
def duplicate(arr):
    ele_count = {}
    duplicates = []

    for num in arr:
        if num in ele_count:
            ele_count[num] += 1
        else:
            ele_count[num] = 1

    for num, count in ele_count:
        if count > 1:
            duplicates.append[num]
    return duplicates

arr = [1,2,2,5,3,7,7,8]
res = duplicate(arr)
print(res)
"""

