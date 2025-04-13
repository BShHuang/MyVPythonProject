from vpython import *
"""
    1. 參數設定
"""
size=1           
g=9.8
m1=1           
m2=2     
y1=20       
y2=18

"""
    2. 畫面設定
"""
scene = canvas(width=400, height=600, center = vec(0,y1,0),background=vec(0.6,0.8,0.8))
floor = box(length=15, height=0.01, width=10, color=color.blue)
ball1 = sphere(radius = size, color=color.yellow ) 
ball2 = sphere(radius = size, color=color.green ) 

ball1.pos = vector(0,y1, 0)         
ball1.v = vector( 0, 0, 0)        
ball2.pos = vector( 0, y2, 0)             
ball2.v = vector( 0, 0, 0)

y1_lab = label(pos=vec(8.0,20.0,0), box = True , color = color.black)
y2_lab = label(pos=vec(8.0,12.0,0), box = True , color = color.black)
v1_lab = label(pos=vec(8.0,16.0,0), box = True , color = color.black)
v2_lab = label(pos=vec(8.0,8.0,0), box = True , color = color.black)
"""
    3. 執行迴圈
"""
t=0
dt = 0.001

while True:             
    rate(1/dt)
    t+=dt

    ball1.pos+=ball1.v*dt
    ball2.pos+=ball2.v*dt
    ball1.v.y+=-g*dt
    ball2.v.y+=-g*dt


    if ball1.pos.y<=size and ball1.v.y<0:
        ball1.v = -ball1.v
    if ball2.pos.y<=size and ball2.v.y<0:
        ball2.v = -ball2.v
    if mag(ball1.pos-ball2.pos) <= 2*size  :
        v1y = (m1-m2)*ball1.v.y/(m1+m2) + 2*m2*ball2.v.y/(m1+m2)
        v2y = 2*m1*ball1.v.y/(m1+m2)+ (m2-m1)*ball2.v.y/(m1+m2)    
        ball1.v = vector (0, v1y , 0)
        ball2.v = vector (0, v2y , 0)

    y1_lab.text = str('y1 = %1.1f m'%ball1.pos.y)
    y2_lab.text = str('y2 = %1.1f m'%ball2.pos.y)
    v1_lab.text = str('v1 = %1.1f m/s'%ball1.v.y)
    v2_lab.text = str('v2 = %1.1f m/s'%ball2.v.y)


    
