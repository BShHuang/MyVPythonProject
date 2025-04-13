from vpython import*

g = 9.8                 #重力加速度 9.8 m/s^2
size = 0.05             #球半徑 0.05 m            
L = 0.5                 #彈簧原長 0.5m
k = 100000             #彈簧力常數 100000 N/m
m = 0.1                 #球質量 0.1 kg
X=0.3
Fg = m*vector(0,-g,0)

def SpringForce(r,L):
    return -k*(mag(r)-L)*r/mag(r)

scene = canvas(width=600, height=600, center=vector(0, -L*0.8, 0))
ball = sphere(radius = size,  color=color.yellow)
ball1 = sphere(radius = size,  color=color.red, make_trail = True, retain = 1000, interval=1)
ball2 = sphere(radius = size,  color=color.green, make_trail = True, retain = 1000, interval=1)
rod1 = cylinder(radius=size/10)
rod2 = cylinder(radius=size/10)

ball1.pos = vector(L,0, 0)   #球的初始位置
ball1.v = vector(0, 0, 0)                            #球初速
rod1.pos = vector(0, 0, 0)
ball2.pos = vector(2*L,0, 0)   #球的初始位置
ball2.v = vector(0, 0, 0)
rod2.pos = vector(L, 0, 0)

gd=graph(title="E-t plot,red for ball1,green for ball2 ",width=600,height=400,xtitle="t",ytitle="energy")
f1=gcurve(color=color.red)
f2=gcurve(color=color.green)

t=0
dt=0.001

while True:
    rate(1/dt)
    t+=dt

    rod2.pos=ball1.pos
    rod2.axis=ball2.pos-ball1.pos
    rod1.axis=ball1.pos-ball.pos
    
    ball1.a=(SpringForce(rod1.axis,L)-SpringForce(rod2.axis,L)+Fg)/m
    ball1.v+=ball1.a*dt
    ball1.pos+=ball1.v*dt

    ball2.a=(SpringForce(rod2.axis,L)+Fg)/m
    ball2.v+=ball2.a*dt
    ball2.pos+=ball2.v*dt

    Ug1 =m * g * (ball1.pos.y+L)
    Us1 = 0.5 * k * (mag(rod1.axis) - L)**2
    K1 = 0.5 * m * mag(ball1.v)**2
    total1=Ug1+Us1+K1

    Ug2 =m * g * (ball2.pos.y+L)
    Us2 = 0.5 * k * (mag(rod2.axis) - L)**2
    K2 = 0.5 * m * mag(ball2.v)**2
    total2=Ug2+Us2+K2

    f1.plot(pos=(t,total1))
    f2.plot(pos=(t,total2))

    
    
    

