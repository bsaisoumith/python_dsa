""" 
N = int(input())
arr = list(map(int, input().split()))

def reverse(arr, N):
    left = 0
    right = N -1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr
"""

""" 
N = int(input())
bin_n = bin(N)[2:]
bin_n = bin_n[::-1]
print(int(bin_n,2)) 
# import math
# k = (1 << (math.log2(N) + 1)) - 1
# print(N ^ k)
"""

""" 
n = int(input())
arr = list(map(int, input().split()))
count = 0
for i in range(n):
    if arr[i] < arr[i + 1]:
        count += 1

print(count)
"""
        
""" 
n = int(input())
mul = 1
while n:
    mul *= (n % 10)
    n = n // 10
print(mul)
"""

""" 
str = input()
n = int(input())
count = 0
max_count = 0
for i in range(len(str)):
    if i % n == 0:
        max_count = max(max_count,count)
        count = 0
    if str[i] == 'a':
        count += 1
if max_count < count:
    max_count = count
print(max_count)  
"""

""" 
n = int(input())
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)
print(fact(n-1)*2)
"""

""" 
def single_digit_sum(n,r):
    if r == 0:
        return 0
    
    def sum_digit(n):
        return sum(int(digit) for digit in str(n))
    
    digit_sum = sum_digit(n)
    repeated_sum = digit_sum * r

    def digital_root(repeated_sum):
        if repeated_sum == 0:
            return 0
        elif repeated_sum % 9 == 0:
            return 9
        else:
            return repeated_sum % 9
    
    return digital_root(repeated_sum)

n = int(input())
r = int(input())
print(single_digit_sum(n,r))
"""

"""   
n = int(input())
r = int(input())
sum = 0
for i in str(n):
    sum += int(i)
sum = sum * r
s = 0
for i in str(sum):
    s += int(i)
print(s) 
"""
""" 
n = int(input())
a = list(map(int, input().split()))
d = int(input())
x = int(input())

even_count = 0
odd_count = 0

for i in range(len(a)):
    if a[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
if d % 2 != 0:
    if even_count == 0:
        print(0)
    else:
        print(even_count * x)
else:
    if odd_count == 0:
        print(0)
    else:
        print(odd_count * x)
"""

""" 
v = int(input())
w = int(input())

if w % 2 != 0 or w <= 2 or v > w:
    print("INVALID INPUT")
else:
    TW = (2 * v - w// 2 )
    FW = v - TW
    print(f"TW = {TW} FW = {FW}")

"""

""" 
s="***##"
a=0
b=0
for i in s:
    if i=='*':
        a+=1
    elif i=='#':
        b+=1
print(a-b) 
"""

""" 
s = input()
count_hash = s.count("#")
count_star = s.count("*")
print(count_hash-count_star)
"""

""" 
N = 10
K = 5
No_of_candies = int(input())
if No_of_candies in range(1, K+1):
    print("NUMBER OF CANDIES SOLD : ",No_of_candies)
    print("NUMBER OF CANDIES AVAILABLE :",N - No_of_candies)
else:
    print("Invalid Input")
    print('No. of Candies Left:',N)

"""

""" 
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

k = k % n
reverse(arr, 0, n - 1)
reverse(arr, 0, k - 1)
reverse(arr, k, n - 1)

print(arr)
"""


""" 
def count_unique_digit_numbers(n1, n2):
    def has_unique_digits(num):
        num_str = str(num)
        digit_set = set()
        for char in num_str:
            if char in digit_set:
                return False
            digit_set.add(char)
        return True

    count = 0
    for num in range(n1, n2 + 1):
        if has_unique_digits(num):
            count += 1
    return count
        
n1 = int(input())
n2 = int(input())
print(count_unique_digit_numbers(n1,n2))
"""

""" 
from itertools import permutations

def find_permutations(number):
    # Convert the number to a string to manipulate its digits
    str_num = str(number)
    # Generate all unique permutations of the digits
    perm = set(''.join(p) for p in permutations(str_num))
    # Convert them back to integers
    perm_ints = [int(p) for p in perm]
    return perm_ints

# Example usage
number = 459
permutations_of_number = find_permutations(number)
print(permutations_of_number)
"""

""" 
# This problem was given to me and i am unable to solve time given: 55 Min
m = int(input())
n = int(input())

def is_prime(i):
    if i <= 1:
        return False
    elif i == 2:
        return True
    elif i % 2 == 0:
        return False
    for j in range(3, int(i ** 0.5) + 1, 2):
        if i % j == 0:
            return False
    return True

if m > n:
    print("Invalid")
else:
    print(f"The prime Numbers from {m} to {n} is: ")
    for i in range(m,n):
        if is_prime(i):
            print(i, end=" ")
"""


