from numpy import *
import math
import matplotlib.pyplot as plt

t = linspace(0, 2*math.pi, 400)
a = sin(t)
b = cos(t)
c = a + b

plt.plot(t, a, label = 'r') # plotting t, a separately 
plt.plot(t, b, label = 'b') # plotting t, b separately 
plt.plot(t, c, label = 'g') # plotting t, c separately 
plt.legend()
plt.xlabel("gitugitu")
plt.ylabel("gitubanget")
plt.title("atitle")
plt.show()