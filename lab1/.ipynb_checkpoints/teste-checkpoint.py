
import numpy as np
import matplotlib.pyplot as plt
n0=24000
w1 = np.zeros(2*n0)
h = np.zeros(2*n0)
h[0]=1
h[n0]=-0.31
w1[0] = 1
w1[n0] = 0.31
w1[4800] = 0.31*0.31
w2 = np.random.rand(2*n0,)
a = np.convolve(w1,h)
print(a)
b = np.convolve(w2,h)
print(b)
x = np.linspace(0, 24000,1)
print(x)
