from vpython import*

size=1
m1=1
m2=2
k=20
L=5
x1=-20
x2=-5
v1=6
v2=3

def SpringForce(r,L):
    return -k*(mag(r)-L)*norm(r)

scene=canvas(width=1000, height=300, background=vec(0.6,0.8,0.8), center=vec(5,0,10))
ball1=sphere(radius=size, color = color.red, make_trail = True,opacity = 0.6)
ball2=sphere(radius=size, color = color.blue, make_trail = True,opacity = 0.6)

ball1.pos=vec(x1,0,0)
ball1.v=vec(v1,0,0)
ball2.pos=vec(x2,0,0)
ball2.v=vec(v2,0,0)

v1_arrow = arrow(pos=ball1.pos,axis=ball1.v,shaftwidth=0.2*size,color = color.red)
v2_arrow = arrow(pos=ball2.pos,axis=ball2.v,shaftwidth=0.2*size,color = color.blue)

x_t = graph(align='left',width=333,height=300,title='x-t', xtitle='t', ytitle='x')
f1_1 = gcurve(color=color.red)       
f1_2 = gcurve(color=color.blue)       
v_t = graph(align='left',width=333,height=300,title='v-t', xtitle='t', ytitle='v')
f2_1 = gcurve(color=color.red)       
f2_2 = gcurve(color=color.blue) 
a_t = graph(align='left',width=333,height=300,title='a-t', xtitle='t', ytitle='a')
f3_1 = gcurve(color=color.red)
f3_2 = gcurve(color=color.blue) 

t=0
dt=0.001

while True:
    rate(1/dt)
    t+=dt
    
    if mag(ball2.pos-ball1.pos)<2*size:
        r=ball2.pos-ball1.pos
        ball1.a=-SpringForce(r,L)/m1
        ball2.a=SpringForce(r,L)/m2
    else:
        ball1.a=vec(0,0,0)
        ball2.a=vec(0,0,0)

    ball1.v+=ball1.a*dt
    ball1.pos+=ball1.v*dt

    ball2.v+=ball2.a*dt
    ball2.pos+=ball2.v*dt

    v1_arrow.pos=ball1.pos
    v1_arrow.axis=ball1.v
    v2_arrow.pos=ball2.pos
    v2_arrow.axis=ball2.v

    f1_1.plot( pos=(t,ball1.pos.x))
    f2_1.plot( pos=(t,ball1.v.x))
    f3_1.plot( pos=(t,ball1.a.x))

    f1_2.plot( pos=(t,ball2.pos.x))
    f2_2.plot( pos=(t,ball2.v.x))
    f3_2.plot( pos=(t,ball2.a.x))
    
    

