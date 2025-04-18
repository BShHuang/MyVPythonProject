from vpython import*
"""
    1. 參數設定
"""
g = 9.8                 #重力加速度
size = 0.05             #球半徑          
L = 0.5                 #棒子原長
k = 100000             #彈簧力常數 
m = 0.1                 #球質量
Fg = m*vec(0,-g,0)   #球所受重力向量

def SpringForce(r,L):
    return -k*(mag(r)-L)*r/mag(r)     #虎克定律
"""
    2. 畫面設定
"""
scene = canvas(align='left',width=600, height=600, center=vec(0, -L*0.8, 0))
ball = sphere(radius = size, color=color.yellow)       #中心
ball1 = sphere(radius = size, color=color.red, make_trail = True, retain = 1000, interval=1)     #球1
ball2 = sphere(radius = size, color=color.green, make_trail = True, retain = 1000, interval=1)   #球2
rod1 = cylinder(radius=size/10)          #中心與球1連接的桿子(內棒)
rod2 = cylinder(radius=size/10)          #球1與球2連接的桿子(外棒)

ball1.pos = vec(L,0, 0)           #球1的初始位置
ball1.v = vec(0, 0, 0)
rod1.pos = vec(0, 0, 0)
ball2.pos = vec(2*L,0, 0)     #球2的初始位置
ball2.v = vec(0, 0, 0)
rod2.pos = vec(L, 0, 0)         #外棒頭在球1處

#畫E-t圖證明總力學能守恆(球1的力學能+球2的力學能)
gd=graph(align='right',title="E-t plot,red for ball1,green for ball2 ",width=600,height=400,xtitle="t",ytitle="energy")
f1=gcurve(color=color.red)
f2=gcurve(color=color.green)
"""
    3. 執行迴圈
"""
t=0
dt=0.001

while True:
    rate(1/dt)
    t+=dt

    rod2.pos=ball1.pos          #外棒頭在球1處
    rod2.axis=ball2.pos-ball1.pos        #內棒的軸方向由原點指向球1
    rod1.axis=ball1.pos-ball.pos           #外棒的軸方向由球1指向球2
    
    ball1.a=(SpringForce(rod1.axis,L)-SpringForce(rod2.axis,L)+Fg)/m    #球1所受合力=內棒張力+外棒張力+重力
    ball1.v+=ball1.a*dt
    ball1.pos+=ball1.v*dt

    ball2.a=(SpringForce(rod2.axis,L)+Fg)/m     #球2所受合力=外棒張力+重力
    ball2.v+=ball2.a*dt
    ball2.pos+=ball2.v*dt
    '''
        畫圖表
    '''
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

    
    
    

