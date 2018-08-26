
# coding: utf-8

# #### 2D 

# In[1]:


import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import mpl_toolkits.mplot3d
from mpl_toolkits.mplot3d import Axes3D
import scipy as sp
get_ipython().magic('matplotlib notebook')


# In[2]:


L=3
xs = np.arange(0, L, 0.01)
ys = np.arange(0, L, 0.01)
X, Y = np.meshgrid(xs, ys) 


# In[3]:


def psiPIB(n,x,m,y):
    return (2/L)*np.sin(sp.pi*x*n/L)*np.sin(sp.pi*y*m/L)


# In[4]:


def main():
    a=1
    n1=int(input('n?'))
    m1=int(input('m?'))
    z=psiPIB(n1,X,m1,Y)
    while True:
        n1=input('n?')
        if n1 =='done':
            break
        else:
            m1=input('m?')
            a+=1
            z+=psiPIB(int(n1),X,int(m1),Y)
    Z=z/sp.sqrt(a)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(X,Y,Z,cmap='rainbow')
    plt.show()
    
            
        


# In[8]:


main()

