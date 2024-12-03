# For outer loop, count the No. of lines
# for the inner loop, focus on the columns and connect them somehow to the rows
# print them inside the inner for loop
# observe symmetry in some cases of patterns


def print1(n):
    for i in range(0,n):
        for j in range(0,n):
            print("*",end=" ")
        print("\r")
    
def print2(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")

'''
#using recursion
def pypart(n):
    if n==0:
        return
    else:
        pypart(n-1)
        print("* "*n)
'''

def print3(n):
    for i in range(1,n+1):
        print(" " * (n - i) +"*" * i)

def print4(n):
    # number of spaces
    k = n - 1
 
    # outer loop to handle number of rows
    for i in range(0, n):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
     
        # decrementing k after each loop
        k = k - 1
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("* ", end="")
     
        # ending line after each row
        print("\r")
    
def print5(n):
    num = 1
    for i in range(0,n):
        num = 1
        for j in range(0,i+1):
            print(num, end=" ")
            num += 1
        print("\r")


def print6(n):
    num = 1
    for i in range(0,n):
        for j in range(0,i+1):
            print(num,end=" ")
            num += 1
        print("\r")
    
def print7(n):
    num = 65
    for i in range(0,n):
        for j in range(0,i+1):
            ch = chr(num)
            print(ch,end=" ")
        num += 1
        print("\r")

def print8(n):
    num = 65
    for i in range(0,n):
        for j in range(0,i+1):
            ch = chr(num)
            print(ch,end=" ")
            num += 1
        print("\r")

def print9(n):
    num = 65
    for i in range(0,n):
        num = 65
        for j in range(0,i+1):
            ch = chr(num)
            print(ch,end=" ")
            num += 1
        print("\r")

def print10(n):
    num = 65
    for i in range(0,n):
        print(" " * (n-i), end=" ")
        for j in range(0,i+1):
            ch = chr(num)
            print(ch,end=" ")
            num += 1
        print("\r")

def print11(n):
    for i in range(0,n):
        for j in range(0,n):
            print("*",end=" ")
        print("\r")
        n -= 1

def print12(n):
    for i in range(n,0,-1):
        for j in range(n-i):
            print(' ', end='') # printing space and staying in same line
        
        for j in range(2*i-1):
            print('*',end='') # printing * and staying in same line
        print() # printing new line

def print13(n):
    for l in range(n,0,-1):
        for i in range(n,0,-1):
            for j in range(l):
                print(i,end=" ")
            print("$",end="")
    print()

def print14(N):
    for i in range(N):
        x=1
        for j in range(2*N-1):
            if(i+j<N-1 or i+j>=N+2*i):   
                print(" ",end="")
            else:
                print(x,end="")
                x+=1 
        print()
    for i in range(N-1):
        x=1
        for j in range(2*N-1):
            if(i+j<=2*i or i+j>=(2*N-2)):      
                print(" ",end="")
            else:
                print(x,end="")
                x+=1 
        print()

def print15(N):
    for i in range(N, 0, -1):
        print(" " * (N - i) + "* " * i)

    for i in range(2, N + 1):
        print(" " * (N - i) + "* " * i)

if __name__ == '__main__':
    n = int(input())
    print1(n); print2(n); print3(n); print4(n); print5(n); print6(n)
    print7(n); print8(n); print9(n); print10(n); print11(n); print12(n); print13(n); print14(n); print15(n)


    