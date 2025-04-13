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
wall1 = box (pos=vec(-5,0,0), length=0.5, height=4, width=4, color=color.blue)
wall2 = box (pos=vec(25,0,0), length=0.5, height=4, width=4, color=color.blue)

ball1 = sphere(radius = size, color=color.yellow ) 
ball2 = sphere(radius = size, color=color.green ) 

ball1.pos = vector( x1, 0, 0)         
ball1.v = vector( v1, 0, 0)        
ball2.pos = vector( x2, 0, 0)             
ball2.v = vector( v2, 0, 0)          

v1_lab = label(pos=vec(2.0,5.0,0), box = True , color = color.black)
v2_lab = label(pos=vec(2.0,3.0,0), box = True , color = color.black)
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

    if ball1.pos.x > 25 or ball1.pos.x < -5:
        ball1.v = -ball1.v
    if ball2.pos.x > 25 or ball2.pos.x < -5:
        ball2.v = -ball2.v
    if mag(ball1.pos-ball2.pos) <= 2*size  :
        v1x = (m1-m2)*ball1.v.x/(m1+m2) + 2*m2*ball2.v.x/(m1+m2)
        v2x = 2*m1*ball1.v.x/(m1+m2)+ (m2-m1)*ball2.v.x/(m1+m2)    
        ball1.v = vector (v1x , 0 , 0)
        ball2.v = vector (v2x , 0 , 0)   

    v1_lab.text = str('v1 = %1.1f m/s'%ball1.v.x)
    v2_lab.text = str('v2 = %1.1f m/s'%ball2.v.x)

    
