
# coding: utf-8

# In[1]:

from vpython import *


# In[2]:

from math import *


# In[3]:

xaxis=curve(vec(-5,0,0),vec(5,0,0))
yaxis=curve(vec(0,-5,0),vec(0,5,0))


# In[4]:

a=2
delta_phi=0


# In[5]:

phasor1=arrow(pos=vec(0,0,0),axis=vec(2,0,0),color=color.green)
phasor2=arrow(pos=phasor1.axis,axis=vec(a*cos(delta_phi),a*sin(delta_phi),0),color=color.red)
phasor3=arrow(pos=phasor2.axis+phasor1.axis,axis=vec(a*cos(2*delta_phi),a*sin(2*delta_phi),0),color=color.blue)
phasor_sum=arrow(pos=vec(0,0,0),axis=phasor1.axis+phasor2.axis+phasor3.axis,color=color.white)


# In[ ]:

omega=0.1
dt=1
while True:
    rate(30)
    phasor2.axis=vec(a*cos(delta_phi),a*sin(delta_phi),0)
    delta_phi=delta_phi+omega*dt
    phasor3.axis=vec(a*cos(2*delta_phi),a*sin(2*delta_phi),0)
    phasor3.pos=pos=phasor2.axis+phasor1.axis
    delta_phi=delta_phi+omega*dt
    phasor_sum.axis=phasor1.axis+phasor2.axis+phasor3.axis
   




