

from vpython import*


from math import*
canvas(forward=vec(-1,-1,-1),up=vec(0,0,1))
xyplane=box(pos=vector(0,0,0),length=10,width=10,height=0.1,color=color.white,opacity=0.5)
yzplane=box(pos=vector(0,0,0),length=0.1,width=10,height=10,color=color.yellow,opacity=0.5)
xyplane=box(pos=vector(0,0,0),length=10,width=0.1,height=10,color=color.yellow,opacity=0.5)
label(pos=vec(6,0,0),text='x')
label(pos=vec(0,6,0),text='y')
label(pos=vec(0,0,6),text='z')



particle=sphere(pos=vector(0,0,0),radius=0.5,color=color.red,charge=5)


source=sphere(pos=vector(2,0,0),radius=0.4,color=color.blue,charge=4)


label(pos=source.pos,text="this is the source")


r_source=particle.pos-source.pos

print(r_source) 

obs=sphere(pos=vector(3,2,0),radius=0.25,color=color.green)

label(pos=obs.pos,text='this is the observation point ')

r=obs.pos-source.pos

print(r)

r_hat=r/mag(r)

print (r_hat)

pointer=arrow(pos=obs.pos,axis=r,shaftwidth=0.1)

k=1


F_vector=k*source.charge*r_hat/(mag(r)**2)
print(F_vector)

