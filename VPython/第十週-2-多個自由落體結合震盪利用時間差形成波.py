from vpython import *
"""
    1. 參數設定
"""
g = 9.8         #重力加速度
k = 80.0        #彈力常數
L0 = 0.6        #彈簧原長
H = 1.5         #球的初始高度
m = 0.5         #球的質量
d = 0.15        #震盪子的水平間距
size = 0.06     #球的大小
n = 40           #球的個數
T = 0.05        #相鄰兩球落下的時間差
def SpringForce(r,L):    #彈力
    return -k*(mag(r)-L)*r/mag(r)
"""
    2. 畫面設定
"""
scene = canvas(width=800, height=400, center=vec(d*n/2-d/2,L0,0))
floor = box(length=d*n, height=0.005, width=0.3, color=color.yellow, pos=vec(d*n/2-d/2,0,0))    #畫地板

#畫40顆球和彈簧
ball=[]
spring=[]
for i in range(n):
    ball.append(sphere(radius = size, color=color.red, pos=vec(i*d,H,0), v=vec(0,0,0)))
    spring.append(helix(radius=0.03, thickness=0.01, pos=vec(i*d,0,0), axis=vec(0,L0,0)))

touched = [False]*n         #設定40顆球是否接觸到彈簧的判斷，初始設定為沒碰到(False)
"""
    3. 執行迴圈
"""
dt = 0.001    #時間間隔
t = 0                #初始時間
while True:
    rate(1/dt/3)        #以1/3的速度慢速模擬
    t = t + dt          #計時器

    #每隔T秒落一顆
    a=[]
    for j in range(n):
        if t < j*T:
            a.append(vec(0,0,0))
        else:
            a.append(vec(0,-g,0))

        if ball[j].pos.y - spring[j].pos.y - spring[j].axis.y <= size:      #球的下緣接觸到彈簧的條件
            touched[j] = True    #接觸到了，將原先預設False改為True
        if touched[j]:
            spring[j].axis = ball[j].pos-spring[j].pos - vec(0,size,0)   #球接觸到彈簧之後，將彈簧的尾端鎖在球的下緣

        a[j] += SpringForce(spring[j].axis,L0)/m     #球的加速度
        ball[j].v += a[j]*dt                                                   #球的速度
        ball[j].pos += ball[j].v*dt           #球的位置
