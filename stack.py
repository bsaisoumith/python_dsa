'''
# list is not correct approach for stack implementation
# because when exceeds it capacity it reallocates new memory location with aditional of 2*capacity
s = []
s.append('https://www.cnn.com/')
s.append('https://www.cnn.com/world')
s.append('https://www.cnn.com/india')
s.append('https://www.cnn.com/china')

print(s)
s.pop()
'''

# collections.deque which is list-like container with fast appends and pops on either end

'''
from collections import deque
stack = deque()

stack.append('https://www.cnn.com/')     # Add x to the right ide of the deque 
stack.append('https://www.cnn.com/world')
stack.append('https://www.cnn.com/india')
stack.append('https://www.cnn.com/china')

print(stack)
print(stack.pop()) 
print(stack.pop())
'''

class STACK:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# creating class stack

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)

def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ''
    while stack.size()!=0:
        rstr += stack.pop()

    return rstr

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2
    
def parentheses_check(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size() == 0


if __name__ == '__main__':
    s = Stack()

    s.push(5)
    s.push(10)
    s.push(15)
    s.push(20)
    print(s.container)

    s.pop()
    print(s.peek())
    print(s.size())
    print(("Reverse string of 'I am a Legend' is:"),reverse_string("I am a Legend"))
    print(("Reverse string of 'PSPK forever' is:"),reverse_string("PSPK forever"))
    
    print(parentheses_check("(a+b)/c"))
    print(parentheses_check("{[]}(a+b)"))
    print(parentheses_check("{([)})"))


