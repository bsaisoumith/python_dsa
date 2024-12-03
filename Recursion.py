# sum of n numbers using recursion
"""
def find_sum(n):
    #sum = 0
    #for i in range(1,n+1):
    #    sum += i
    #return sum 

    if n == 1:
        return 1
    return n + find_sum(n-1)

print(find_sum(5)) 
"""

# fibonacci series
""" 
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)

def generateFib(n): 
    fib = [0,1]

    for i in range(2,n):
        fib.append(fib[i-1] + fib[i-2])

    return fib[:n]    

print(fib(1))
s = generateFib(1)
print(s)
for i in range(0,len(s)):
    print(s[i],end=" ")
"""

#factorial
""" 
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n*fact(n-1)

n = int(input())
print(fact(n))
"""

#palindrome
""" 
def isPalindrome(string):
    size = len(string)

    if size < 1:
        return True

    if string[0] != string[size-1]:
        return False

    return isPalindrome(string[1:-1])

string = input()
string = string.lower()
string = ''.join(filter(str.isalnum,string))
print(isPalindrome(string))
"""

#GCD of two numbers
""" 
def gcd(a,b):
    if(b == 0):
        return a
    return gcd(b, a % b)

print('gcd of two numbers is:',gcd(98,56)) """






