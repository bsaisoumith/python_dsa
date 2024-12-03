"""
# using a list 
stock_prices = []
with open("stock_prices.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices.append([day,price])
        
print(stock_prices)

for element in stock_prices:    # it takes order of n i.e O(n) for finding nth price of stack of nth day
    if element[0] == 'march 9':
        print(element[1])
    
"""

"""
stock_prices = {}        # using dictonary
with open("stock_prices.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price
        
print(stock_prices)

stock_prices['march 9']  # O(1) complexity

# in hash function look by key us O(1) on average
# insertion/deletion is O(1) on average

"""
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def add(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None

    def print(self):
        print(self.arr)

    
t = HashTable()
t.add('march 6',138)
t.get('march 6')
t.print()

t['march 8'] = 145   # calls __setitem__
print(t['march 8'])         # calls __getitem__

del t['march 8']
print(t.arr)