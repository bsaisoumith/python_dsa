"""
Numpy's most useful feature is n dimentional array object(a.k.a ndarray)
3 main benefits of numpy array over a python list, (1) Less Memory (2) Fast (3) Convinient 
"""

import numpy as np
import time
import sys

l = range(1000)
print(sys.getsizeof(5)*len(l))

array = np.arange(1000)
print(array.size*array.itemsize)

SIZE = 10000000

l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print("Python List took: ",(time.time() - start)*1000)

start = time.time()
result = a1 + a2
print("Numpy took: ",(time.time() - start)*1000)

a = np.array([5,6,7])
b = np.array([[1,2],[3,4],[5,6]])
print(a.ndim,b.ndim)   # to know about dimensions

a = np.array([[1,2],[3,4],[5,6]], dtype = np.float64)
print(a.itemsize)
a = np.array([[1,2],[3,4],[5,6]], dtype = np.complex64)
print(a,a.itemsize)


print(np.zeros((3,4)),"\n",np.ones((3,4)))
print(np.arange(1,5), np.arange(1,5,2),"\n", np.linspace(1,5,10))

a = np.array([[1,2],[3,4],[5,6]])
a.reshape(6,1)  # to reshape the array
a.ravel()    # to flatten the array
print(a.max(),a.min(),a.sum())
print(a.sum(axis=0),a.sum(axis=1))
print(np.sqrt(a),np.std(a))  #std is a standard deviation
print(a+b,a-b,a*b) 

a = np.array([[6,7,8], [1,2,3], [9,3,2]])
for row in a:
    print(row)
for cell in a.flat:
    print(cell)


a = np.arange(6).reshape(3,2)
b = np.arange(6,12).reshape(3,2)  
print(a,"\n",b)
print(np.vstack((a,b))) # to stack them together 
print(np.hstack((a,b)))

a = np.arange(12).reshape(3,4)
for x in np.nditer(a,order = 'C'):  # C order printing row by row
    print(x)
for x in np.nditer(a,order = 'F'):  # Fortran order prinitng column by column
    print(x)
for x in np.nditer(a,order = 'F', flags = ['external_loop']): 
    print(x)
for x in np.nditer(a,order = 'F', op_flags = ['readwrite']): 
    x[...] = x*x
print(a)

b = np.arange(3,15,4).reshape(3,1)
for x,y in np.nditer([a,b]):
    print(x,y)
 
