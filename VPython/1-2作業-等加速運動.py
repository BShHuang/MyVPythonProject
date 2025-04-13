from vpython import*

scene=canvas(width=600,height=400,center=vector(2.5,0,0),background=vector(0,0,0))
x=arrow(pos=vector(0,0,0),axis=vector(1,0,0),color=color.green)
y=arrow(pos=vector(0,0,0),axis=vector(0,1,0),color=color.red)
z=arrow(pos=vector(0,0,0),axis=vector(0,0,1),color=color.blue)
ball=sphere(radius=0.1,color=color.orange,pos=vector(0,0,0),v=vector(3,0,0),a=vector(-1,-0.5,0))

gd=graph(title="x-t plot",width=600,height=400,xtitle="t",ytitle="x")
f1=gcurve(color=color.blue)
gd2=graph(title="v-t plot",width=600,height=400,xtitle="t",ytitle="v")
f2=gcurve(color=color.red)
gd3=graph(title="a-t plot",width=600,height=400,xtitle="t",ytitle="a")
f3=gcurve(color=color.green)

t=0
dt=0.001

while t<4:
    rate(1/dt)
    t+=dt
    ball.pos+=ball.v*dt
    ball.v+=ball.a*dt

    if ball.v.x>0 and ball.v.x+ball.a.x*dt<=0:
        print(t)
        print(ball.pos)
        print(ball.v)
    
    plotT=t%0.4
    if plotT<0.4 and plotT+dt>=0.4:
        arrow(color=color.purple, pos=ball.pos, axis=ball.v, shaftwidth=0.05)    #畫速度箭頭
        arrow(color=color.yellow, pos=ball.pos, axis=ball.a, shaftwidth=0.05)    #畫加速度箭頭
        sphere(color=color.orange, pos=ball.pos, radius=0.1) 
