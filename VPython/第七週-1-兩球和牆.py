from vpython import *
"""
    1. 參數設定
"""
size = 1              #球半徑 
m1 = 2               #球1質量  
m2 = 1              #球2質量  
x1 = 0          #球1初始位置
v1 = 6              #球1初速度
x2 = 10       #球2初始位置
v2 = 7            #球2初速度

"""
    2. 畫面設定
"""
scene = canvas(width=1000, height=400, center = vec(10,0,0), background=vec(0.6,0.8,0.8))
wall1 = box (pos=vec(-5,0,0), length=0.5, height=4, width=4, color=color.blue)       #畫左牆
wall2 = box (pos=vec(25,0,0), length=0.5, height=4, width=4, color=color.blue)      #畫右牆

ball1 = sphere(radius=size, color=color.yellow, pos=vec(x1,0,0), v=vec(v1,0,0))       #畫球1
ball2 = sphere(radius=size, color=color.green, pos=vec(x2,0,0), v=vec(v2,0,0))         #畫球2

v1_lab = label(pos=vec(2.0,5.0,0), box = True , color = color.black)      #顯示球1速度
v2_lab = label(pos=vec(2.0,3.0,0), box = True , color = color.black)      #顯示球2速度
"""
    3. 執行迴圈
"""
dt = 0.001

while True:             
    rate(1/dt)

    ball1.pos+=ball1.v*dt
    ball2.pos+=ball2.v*dt

    if ball1.pos.x > 25 or ball1.pos.x < -5:         #碰到牆就反彈(速度變號但大小不變)
        ball1.v = -ball1.v
    if ball2.pos.x > 25 or ball2.pos.x < -5:
        ball2.v = -ball2.v
    if mag(ball1.pos-ball2.pos) <= 2*size  :       #兩球碰撞就代撞後速度公式
        v1x = (m1-m2)*ball1.v.x/(m1+m2) + 2*m2*ball2.v.x/(m1+m2)
        v2x = 2*m1*ball1.v.x/(m1+m2)+ (m2-m1)*ball2.v.x/(m1+m2)    
        ball1.v = vec(v1x , 0 , 0)
        ball2.v = vec(v2x , 0 , 0)   

    v1_lab.text = str('v1 = %1.1f m/s'%ball1.v.x)
    v2_lab.text = str('v2 = %1.1f m/s'%ball2.v.x)

    
