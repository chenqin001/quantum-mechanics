
# coding: utf-8

# In[1]:

from math import *
import scipy as sp
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib notebook')


# In[2]:

x=sp.linspace(-2,2,201)

print(x)
# In[3]:

y=x**3


# In[4]:

print(y)


# In[5]:

def f1(x):
    return x**3


# In[6]:

plt.figure()
plt.plot(x,y)
plt.xlabel('Label for horizonal axis')
plt.ylabel('Label for vertical axis')
plt.title('this is the title')
plt.axhline(0)
plt.grid(True)
plt.ylim(-12,12)


# In[33]:

x=sp.linspace(0,1,201)
v=1

A=1
L=1
m=1
lamda=2*L/m
f=v/lamda
omega=sp.pi*2*f
t=2
def f2(x):
    return A*sp.sin(sp.pi*2*x/lamda)*cos(omega*t)


# In[36]:

plt.figure()
plt.plot(x,f2(x))
plt.xlabel('x')
plt.ylabel('y(x,t)')
plt.title('standing waves')
plt.axhline(0)
plt.grid(True)
plt.ylim(-2,2)



