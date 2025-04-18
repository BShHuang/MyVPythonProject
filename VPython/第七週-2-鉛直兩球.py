from vpython import *
"""
    1. 參數設定
"""
size=1           #球半徑 
g=9.8        #重力加速度
m1=1           #球1質量
m2=2           #球2質量
y1=20       #球1初始位置 
y2=18       #球2初始位置
"""
    2. 畫面設定
"""
scene = canvas(width=400, height=600, center = vec(0,y1,0),background=vec(0.6,0.8,0.8))
floor = box(length=15, height=0.01, width=10, color=color.blue)             #畫地板
ball1 = sphere(radius=size, color=color.yellow, pos=vec(0,y1,0), v=vec(0,0,0))       #畫球1
ball2 = sphere(radius=size, color=color.green, pos=vec(0,y2,0), v=vec(0,0,0))         #畫球2

y1_lab = label(pos=vec(8.0,20.0,0), box = True , color = color.black)     #顯示球1高度
v1_lab = label(pos=vec(8.0,16.0,0), box = True , color = color.black)     #顯示球1速度
y2_lab = label(pos=vec(8.0,12.0,0), box = True , color = color.black)     #顯示球2高度
v2_lab = label(pos=vec(8.0,8.0,0), box = True , color = color.black)        #顯示球2速度
"""
    3. 執行迴圈
"""
dt = 0.001

while True:             
    rate(1/dt)

    ball1.pos+=ball1.v*dt
    ball2.pos+=ball2.v*dt
    ball1.v.y+=-g*dt     #兩球皆受重力
    ball2.v.y+=-g*dt

    if ball1.pos.y<=size and ball1.v.y<0:     #碰到地板就反彈(速度變號但大小不變)
        ball1.v = -ball1.v
    if ball2.pos.y<=size and ball2.v.y<0:
        ball2.v = -ball2.v
    if mag(ball1.pos-ball2.pos) <= 2*size  :     #兩球碰撞就代撞後速度公式
        v1y = (m1-m2)*ball1.v.y/(m1+m2) + 2*m2*ball2.v.y/(m1+m2)
        v2y = 2*m1*ball1.v.y/(m1+m2)+ (m2-m1)*ball2.v.y/(m1+m2)    
        ball1.v = vec(0, v1y , 0)
        ball2.v = vec(0, v2y , 0)

    y1_lab.text = str('y1 = %1.1f m'%ball1.pos.y)
    y2_lab.text = str('y2 = %1.1f m'%ball2.pos.y)
    v1_lab.text = str('v1 = %1.1f m/s'%ball1.v.y)
    v2_lab.text = str('v2 = %1.1f m/s'%ball2.v.y)


    
