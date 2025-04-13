from vpython import*

size=0.5
m=1.0
g=9.8
v0=10
theta=pi/4
height=15
k=0.5

scene=canvas(width=600,height=400,center=vector(0,height/2,0),background=vector(0,0,0))
ball=sphere(radius=size,color=color.yellow,make_trail=True,trail_type="points",interval=100)
ball2=sphere(radius=size,color=color.red,make_trail=True,trail_type="points",interval=100)
floor=box(length=20,width=10,height=0.01,color=color.green)

ball.pos=vector(0,size,0)
ball.v=vector(v0*cos(theta),v0*sin(theta),0)
ball.a=vector(0,-m*g,0)/m

ball2.pos=vector(0,size,0)
ball2.v=vector(v0*cos(theta),v0*sin(theta),0)


dt=0.001
t=0

while True:
    rate(1/dt)
    t+=dt
    
    ball.pos+=ball.v*dt
    ball.v+=ball.a*dt
    if ball.pos.y<=size and ball.v.y<0:
        ball.v.y=-ball.v.y

    ball2.a=(-k*ball2.v+vector(0,-m*g,0))/m
    ball2.pos+=ball2.v*dt
    ball2.v+=ball2.a*dt
    if ball2.pos.y<=size and ball2.v.y<0:
        ball2.v.y=-ball2.v.y
        ball2.a=(-k*ball2.v+vector(0,-m*g,0))/m


        
    
        
