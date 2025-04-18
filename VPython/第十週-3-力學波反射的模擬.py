from vpython import *
"""
    1. 參數設定
"""
A = 0.4            #振幅
N = 50             #介質個數
omega = 2*pi/1.0   #振動角頻率
size = 0.1         #介質的大小
m = 0.1            #介質的質量
k = 500.0          #每一小段彈簧的彈力常數
d = 0.4            #介質之間的初始間隔
def SpringForce(r):    #彈力
    return - k*(mag(r)-d)*r/mag(r)
"""
    2. 畫面設定
"""
scene = canvas(title='Spring Wave', width=1200, height=300, range = 0.4*50/6, center = vec((N-1)*d/2, 0, 0)) 
ball = [sphere(radius=size, color=color.yellow, pos=vec(i*d, 0, 0), v=vec(0,0,0)) for i in range(N)]
#以list comprehensions方式產生N個球
spring = [helix(radius = size/2.0, thickness = d/15.0, pos=vec(i*d, 0, 0), axis=vec(d,0,0)) for i in range(N-1)]
#以list comprehensions方式產生N-1條彈簧
"""
    3. 執行迴圈
"""
t, dt = 0, 0.001
while True:
    rate(1000)
    t += dt

    ball[0].pos = vec(0,A*sin(omega*t), 0)    #(模擬橫波)先讓第一個球沿y方向振動
##    ball[0].pos = vec(A*sin(omega*t), 0, 0)    #(模擬縱波)先讓第一個球沿x方向振動

    #在球與球之間放入彈簧
    for i in range(N-1):
        spring[i].pos = ball[i].pos
        spring[i].axis = ball[i+1].pos - ball[i].pos

    #計算每一個球受相鄰兩條彈簧的彈力
    for i in range(1, N):      #第一個球已經設定過了，所以從第二個球開始
        if i == N-1:
            ball[-1].v += SpringForce(spring[-1].axis)/m*dt                            #最後一個球
        else:
            ball[i].v += (-SpringForce(spring[i].axis) + SpringForce(spring[i-1].axis))/m*dt  #非最後且非第一個的球

        ball[i].pos += ball[i].v*dt

    ball[-1].pos.x=(N-1)*d # (模擬自由端反射)需固定最後一顆x位置，否則會被第一顆球的作用力扯亂
##    ball[-1].pos=vec((N-1)*d,0,0)# (模擬固定端反射)
    
