from vpython import*

m=1.0
g=9.8
height=15
size=0.5

scene=canvas(width=600,height=400,center=vector(0,height/2,0),background=vector(0,0,0))
ball=sphere(radius=size,color=color.yellow,make_trail=True,trail_type="points",interval=100)
floor=box(length=20,width=10,height=0.01,color=color.green)

ball.pos=vector(0,height,0)
ball.v=vector(0,0,0)
ball.a=vector(0,-m*g,0)

dt=0.001
t=0

while ball.pos.y>size:
    rate(1/dt)
    t+=dt
    ball.pos+=ball.v*dt
    ball.v+=ball.a*dt
    
