import numpy as np 
import time
'''short lab to discover and getting familiar with numpy'''

a = np.zeros(4)
a = np.arange(32).reshape((2,4,4))

a = np.zeros((4,))
b = np.arange(4.)
# a = np.random.rand(4); 

print(a)
print(b)

a = np.arange(4.);              print(f"np.arange(4.):     a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

a = np.array([5,4,3,2]);  print(f"np.array([5,4,3,2]):  a = {a},     a shape = {a.shape}, a data type = {a.dtype}")

a = np.arange(10)
print(a)
start  = 1
end = 5
print(a[start:end])

c = np.array([1,4,3])
print(c.mean())
print(c.max())
print(c.min())
print(c.sort())


x = np.array([[1, 2],[2, 2],[3, 2],[4, 0]])
y = np.zeros(x.shape)
print(x.shape)
print(y)

a = np.arange(6).reshape(-1, 2)   #reshape is a convenient way to create matrices
print(f"a.shape: {a.shape}, \na= {a}")

m = "hello"
m = 'f'
print(type(m))