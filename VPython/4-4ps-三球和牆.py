
from vpython import *  #引用視覺畫套件Vpython
"""
    1. 參數和公式設定
"""
size = 2              #球半徑 
m1 = 6               #球1質量  
m2 = 2               #球2質量
wall_a=200     #球撞牆時受反方向極大的加速度
r1 = vec(-5,0.5,0)           #球1初始位置
v_1 = vec(6,0,0)              #球1初速度
r2 = vec(5,0,0)        #球2初始位置
v_2 = vec(0,0,0)              #球2初速度

# 定義3維碰撞公式
def three_D_col_for(v1, v2, r1, r2):
    v1_col = v1 - (2*m2/(m1+m2))*dot((v1 - v2), (r1 - r2)) * (r1-r2) / mag2(r1 - r2) 
    v2_col = v2 - (2*m1/(m1+m2))*dot((v2 - v1), (r2 - r1)) * (r2-r1) / mag2(r2 - r1)
    return (v1_col, v2_col)
"""
    2. 畫面設定
"""
scene = canvas(width=800, height=800, center = vec(0,0,0), background=vec(0.6,0.8,0.8),range=15) 

wall_1 = box (pos=vec(-10,0,0), length=0.5, height=20, width=0.5, color=color.blue)
wall_2 = box (pos=vec(10,0,0), length=0.5, height=20, width=0.5, color=color.blue)
wall_3 = box (pos=vec(0,10,0), length=20, height=0.5, width=0.5, color=color.blue)
wall_4 = box (pos=vec(0,-10,0), length=20, height=0.5, width=0.5, color=color.blue)

ball_1 = sphere(radius = size, color=color.yellow , pos = r1 ,v = v_1)
ball_2 = sphere(radius = size, color=color.green , pos = r2 , v = v_2) 

v1_arrow = arrow(pos=ball_1.pos,axis=ball_1.v,shaftwidth=0.2*size ,color = color.yellow) 
v2_arrow = arrow(pos=ball_2.pos,axis=ball_2.v,shaftwidth=0.2*size ,color = color.green)  

"""
    3. 執行迴圈
"""
t=0
dt = 0.001

while True:             
    rate(1/dt)
    t+=dt

    ball_1.pos = ball_1.pos + ball_1.v*dt
    ball_2.pos = ball_2.pos + ball_2.v*dt

    #若兩球球心距離小於兩倍球半徑，則代入碰撞公式改變速度
    if mag(ball_1.pos - ball_2.pos) <= 2*size :
        ball_1.v, ball_2.v = three_D_col_for(ball_1.v, ball_2.v, ball_1.pos, ball_2.pos)

    v1_arrow.pos = ball_1.pos
    v2_arrow.pos = ball_2.pos
    v1_arrow.axis = ball_1.v
    v2_arrow.axis = ball_2.v
    
    if ball_1.pos.x + size > 10 :
        ball_1.v.x = ball_1.v.x  - wall_a*dt
    if ball_2.pos.x + size > 10 :
        ball_2.v.x = ball_2.v.x  - wall_a*dt
    if ball_1.pos.x - size < -10 :
        ball_1.v.x = ball_1.v.x  + wall_a*dt
    if ball_2.pos.x - size < -10 :
        ball_2.v.x = ball_2.v.x  + wall_a*dt

    if ball_1.pos.y + size > 10 :
        ball_1.v.y = ball_1.v.y  - wall_a*dt
    if ball_2.pos.y + size > 10 :
        ball_2.v.y = ball_2.v.y  - wall_a*dt
    if ball_1.pos.y - size < -10 :
        ball_1.v.y = ball_1.v.y  + wall_a*dt
    if ball_2.pos.y - size < -10 :
        ball_2.v.y = ball_2.v.y  + wall_a*dt
