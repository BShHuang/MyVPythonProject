from vpython import*

size=0.5
m=1.0
g=9.8
v0=10
theta=0
height=30
k=0.5

scene=canvas(width=600,height=400,center=vector(0,height/2,0),background=vector(0,0,0))
ball=sphere(radius=size,color=color.yellow,make_trail=True,trail_type="points",interval=1)
floor=box(length=20,width=10,height=0.01,color=color.green)

ball.pos=vector(0,size,0)
ball.v=vector(v0*cos(theta),v0*sin(theta),0)
ball.a=vector(0,-m*g,0)/m

rtheta=graph(title="theta-R plot",width=600,height=400,xtitle="theta",ytitle="R")
c1=gcurve(color=color.red)
Ttheta=graph(title="theta-T plot",width=600,height=400,xtitle="theta",ytitle="T")
c2=gcurve(color=color.blue)



dt=0.001
t=0

while theta<pi:
    rate(1/dt)
    t+=dt
    
    ball.pos+=ball.v*dt
    ball.v+=ball.a*dt
    if ball.pos.y<=size and ball.v.y<0:
        R=ball.pos.x
        T=t
        theta+=pi/60
        ball.pos=vector(0,size,0)
        ball.v=vector(v0*cos(theta),v0*sin(theta),0)
        t=0
        
    show_angle=label(pos=vector(0,-7*size,0),box=False,height=20,color=color.yellow)
    show_angle.text="theta=%1.0f °" %(theta/pi*180)

    c1.plot(pos=(theta,R))
    c2.plot(pos=(theta,T))
