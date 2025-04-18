from vpython import*
"""
    1. 參數設定
"""
size=0.5         #球半徑
m=1                 #球質量1kg
g=9.8              #重力加速度
v0=10             #球初始速度大小
theta=pi/4    #球拋射角度
damp=0.5     #空氣阻力常數
"""
    2. 畫面設定
"""
scene=canvas(width=600,height=400,center=vec(0,7.5,0),background=vec(0,0,0))           #設定背景
ball=sphere(radius=size,color=color.yellow,make_trail=True,trail_type="points",interval=100)  #畫球1和軌跡
ball2=sphere(radius=size,color=color.red,make_trail=True,trail_type="points",interval=100)      #畫球2和軌跡
floor=box(length=20,width=10,height=0.01,color=color.green)      #畫地板

ball.pos=vec(0,size,0)              #球1初始位置
ball.v=vec(v0*cos(theta),v0*sin(theta),0)        #球1初始速度向量
ball.a=vec(0,-m*g,0)/m          #球1加速度(恆為定值g)

ball2.pos=vec(0,size,0)
ball2.v=vec(v0*cos(theta),v0*sin(theta),0)
"""
    3. 執行迴圈
"""
dt=0.001

while True:         #無限迴圈
    rate(1/dt)

    ball.pos+=ball.v*dt
    ball.v+=ball.a*dt
    if ball.pos.y<=size and ball.v.y<0:         #落地就反彈
        ball.v.y=-ball.v.y

    ball2.a=(-damp*ball2.v+vec(0,-m*g,0))/m     #球2受空氣阻力
    ball2.pos+=ball2.v*dt
    ball2.v+=ball2.a*dt
    if ball2.pos.y<=size and ball2.v.y<0:
        ball2.v.y=-ball2.v.y
        ball2.a=(-damp*ball2.v+vec(0,-m*g,0))/m


        
    
        
