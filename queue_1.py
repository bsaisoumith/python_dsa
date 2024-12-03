

'''
# using list
wmt_stock_price_queue = []

wmt_stock_price_queue.insert(0,131.10)
wmt_stock_price_queue.insert(0,132.12)
wmt_stock_price_queue.insert(0,135)

print(wmt_stock_price_queue)

wmt_stock_price_queue.pop()
print(wmt_stock_price_queue)

'''

'''
# using deque from collections

from collections import deque
q = deque()

q.appendleft(5)    # Add x to the left side of the deque
q.appendleft(8)
q.appendleft(10)

print(q)
print(q.pop())
'''


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)



#using class queue

from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            return
        
        return self.buffer.pop()
    
    def front(self):
        return self.buffer[-1]
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)

def binary_numbers(n):
    numbers = Queue()
    numbers.enqueue("1")

    for i in range (n):
        front = numbers.front()
        print("   ", front)
        numbers.enqueue(front + "0")
        numbers.enqueue(front + "1")

        numbers.dequeue()
         

import threading
import time

food_order = Queue()

def place_orders(orders):
    for order in orders:
        print("Placing order for:",order)
        food_order.enqueue(order)
        time.sleep(0.5)


def serve_orders():
    time.sleep(1)
    while True:
        order = food_order.dequeue()
        print("Now serving: ",order)
        time.sleep(2)


if __name__ == '__main__':
    pq = Queue()

    pq.enqueue({'company': 'Wall Mart', 'timestamp': '15 apr, 11.01 AM', 'price': 131.10})
    pq.enqueue({'company': 'Wall Mart','timestamp': '15 apr, 11.02 AM','price': 132})
    pq.enqueue({'company': 'Wall Mart','timestamp': '15 apr, 11.03 AM','price': 135})

    print(pq.buffer)

    print(pq.size())
    print(pq.dequeue())
    print(pq.front())

    binary_numbers(10)

    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_orders, args=(orders,))
    t2 = threading.Thread(target=serve_orders)

    t1.start()
    t2.start()
