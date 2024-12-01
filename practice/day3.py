import time 
import numpy as np

x = np.random.random((100,100))
y = np.random.random((100,100))

#using numpy
t0 = time.time()
z = []
for _ in range(1000) :
    z = x+y
    z = np.maximum(z,0.)

print("took : ",time.time() - t0," seconds")

#doing naive -ly too slow
def naive_add(x, y):
    assert len(x.shape) == 2  
    assert x.shape == y.shape
    x = x.copy()  
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] += y[i, j]
    return x

def naive_relu(x) :
    assert len(x.shape) == 2
    x = x.copy()
    for i in range(x.shape[0]) :
        for j in range(x.shape[1]) :
            x[i][j] = max(x[i][j],0)
    return x

t0 = time.time()

for _ in range(1000) :
    z = naive_add(x,y)
    z = naive_relu(z)

print("took : ",time.time() - t0," seconds")
