

from vpython import *
import scipy as sp
import matplotlib as mpl       
import matplotlib.pyplot as plt
import matplotlib.animation as animation
get_ipython().magic('matplotlib notebook')


lep=0
rep=1
np=101
x=sp.linspace(lep,rep,np)



def u(x):
    return 0



dx=(rep-lep)/(np-1)



def integrate(x):
    e=16 #e is n**2
    y=sp.zeros(len(x))
    y[1]=dx
    for i in range(1,np-1):
        y[i+1]=2*y[i]-y[i-1]+dx**2*(-sp.pi**2*((e-u(x))*y[i]))
    return y


plt.figure()
plt.plot(x,integrate(x))
plt.xlabel('Label for horizonal axis')
plt.ylabel('Label for vertical axis')
plt.title('this is the title')
plt.axhline(0)
plt.grid(True)

