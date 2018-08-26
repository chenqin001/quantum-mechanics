
# coding: utf-8

# In[1]:


from vpython import*


# In[2]:


from math import*
canvas(forward=vec(-1,-1,-1),up=vec(0,0,1))
xyplane=box(pos=vector(0,0,0),length=10,width=10,height=0.1,color=color.white,opacity=0.5)
yzplane=box(pos=vector(0,0,0),length=0.1,width=10,height=10,color=color.yellow,opacity=0.5)
xyplane=box(pos=vector(0,0,0),length=10,width=0.1,height=10,color=color.yellow,opacity=0.5)
label(pos=vec(6,0,0),text='x')
label(pos=vec(0,6,0),text='y')
label(pos=vec(0,0,6),text='z')


# In[3]:


particle=sphere(pos=vector(0,0,0),radius=0.5,color=color.red,charge=5)


# In[4]:


source=sphere(pos=vector(2,0,0),radius=0.4,color=color.blue,charge=4)


# In[5]:


label(pos=source.pos,text="this is the source")


# In[6]:


r_source=particle.pos-source.pos


# In[7]:


print(r_source) 


# In[8]:


obs=sphere(pos=vector(3,2,0),radius=0.25,color=color.green)


# In[9]:


label(pos=obs.pos,text='this is the observation point ')


# In[10]:


r=obs.pos-source.pos


# In[11]:


print(r)


# In[12]:


r_hat=r/mag(r)


# In[13]:


print (r_hat)


# In[14]:


pointer=arrow(pos=obs.pos,axis=r,shaftwidth=0.1)


# In[15]:


k=1


# In[16]:


F_vector=k*source.charge*r_hat/(mag(r)**2)
print(F_vector)

