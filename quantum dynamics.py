
# coding: utf-8

# ## Function animator

# #### Imports and ML customizations

# In[2]:


from vpython import *
import scipy as sp

import matplotlib as mpl     
import matplotlib.pyplot as plt
import matplotlib.animation as animation

get_ipython().magic('matplotlib notebook')
mpl.style.use('classic')
plt.rc('figure', figsize = (6, 4.5))            # Reduces overall size of figures
plt.rc('axes', labelsize=16, titlesize=14)
plt.rc('figure', autolayout = True)             # Adjusts supblot parameters for new size
plt.rcParams['figure.figsize'] = (6,4.5) # Change default size of plots
plt.rcParams['font.size'] = 14           # Change default fontsize for figures
plt.rcParams['figure.autolayout'] = True # Adjusts for changes 

from scipy import special 
from scipy import misc


# #### linear combination of particle-in-a-box states
# 

# In[3]:


x=sp.linspace(0,1,201)
v=1
A=1
L=1
m=1
lamda=2*L/m
f=v/lamda
omega=sp.pi*2*f
t=0

def func(x,t):                          
    return A*sp.sin(sp.pi*2*x/lamda)*cos(omega*t)


# In[4]:


def psiPIB(n,x):
    return sp.sqrt(2.0)*sp.sin(n*sp.pi*x)


# In[5]:


def psiTotal(x,t):
    return (sp.exp(-1j*1*t)*psiPIB(1,x)+sp.exp(-1j*4.0*t)*psiPIB(2,x))/sp.sqrt(2.0)


# In[6]:


def animate(i):
    '''Animation function: Updates time, title (containing time), and data'''    
    dt = 0.1
    t0 = 0
    t = t0 + i*dt
    plt.title("t={0:.2f}".format(t)) 
    line.set_ydata(psiTotal(x,t))  # update the data
    return line,


# In[7]:


N = 201                               # Number of points to plot
                                      # Number of itervals = N-1
t = 0.                                # Initial value of time
x = sp.linspace(0, 1, N)  # Create values of x

fig = plt.figure()
plt.ylim([-3,3])
plt.xlabel('$x$')                    # Label for horizontal axis
plt.ylabel("$\psi$")                  # Label for vertical axis
plt.axhline(0,color='green')       # Makes solid green x-axis

x = sp.linspace(0, 1, N)   # choose density of points based on mode number
line, = plt.plot(x, psiTotal(x,t))


# In[8]:


ani = animation.FuncAnimation(fig, animate, interval = 2000)   # interval --> time between frames
plt.show()


# #### linear combination of harmonic oscillator states 1 (shut down the previous diagram!!!)

# In[13]:


def psiHO(n,x):
    return sp.special.eval_hermite(n,x)*sp.exp(-x**2/2.0)/sp.sqrt(2**n*special.factorial(n)*sp.sqrt(sp.pi))


# In[14]:


def psiTotal1(x,t):
    return (sp.exp(-1j*0.5*t)*psiHO(0,x)+sp.exp(-1j*1.5*t)*psiHO(1,x))/sp.sqrt(2.0)


# In[15]:


def animate(i):
    '''Animation function: Updates time, title (containing time), and data'''    
    dt = 0.1
    t0 = 0
    t = t0 + i*dt
    plt.title("t={0:.3f}".format(t)) 
    line.set_ydata(abs(psiTotal1(x,t))**2)  # update the data
    return line,


# In[16]:


N = 201                               # Number of points to plot
                                      # Number of itervals = N-1
t = 1                               # Initial value of time
x = sp.linspace(-2, 2, N)  # Create values of x

fig = plt.figure()
plt.ylim([-3,3])
plt.xlabel('$x$')                    # Label for horizontal axis
plt.ylabel("$\psi$")                  # Label for vertical axis
plt.axhline(0,color='green')       # Makes solid green x-axis


line, = plt.plot(x, abs(psiTotal1(x,t))**2)


# In[17]:


ani = animation.FuncAnimation(fig, animate, interval = 200)   # interval --> time between frames
plt.show()


# #### linear combination of harmonic osillator states 2 (classical)  (shut down the previous diagram!!!)

# In[19]:


def psiTotal2(x,t):
    alpha=2.0
    m=40
    total=0
    for n in range(m):
        total+=sp.exp(-1j*(0.5+n)*t)*alpha**n*psiHO(n,x)/sp.sqrt(sp.special.factorial(n))
    return sp.exp(-alpha**2/2)*total


# In[23]:


def animate(i):
    '''Animation function: Updates time, title (containing time), and data'''    
    dt = 0.1
    t0 = 0
    t = t0 + i*dt
    plt.title("t={0:.2f}".format(t)) 
    line.set_ydata(abs(psiTotal2(x,t))**2)  # update the data
    return line,


# In[28]:


N = 201                               # Number of points to plot
                                      # Number of itervals = N-1
t = 0                               # Initial value of time
x = sp.linspace(-5, 5, N)  # Create values of x

fig = plt.figure()
plt.ylim([-3,3])
plt.xlabel('$x$')                    # Label for horizontal axis
plt.ylabel("$\psi$")                  # Label for vertical axis
plt.axhline(0,color='green')       # Makes solid green x-axis


line, = plt.plot(x, abs(psiTotal2(x,t))**2)


# In[29]:


ani = animation.FuncAnimation(fig, animate, interval = 400)   # interval --> time between frames
plt.show()

