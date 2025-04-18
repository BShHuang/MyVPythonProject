from vpython import*
"""
    1. 參數設定
"""
G = 6.67           #萬有引力常數
m1 = 10           #大球質量
m2 = 3              #小球質量
R = 10               #兩球距離(=大球軌跡半徑r1+小球軌跡半徑r2)
def Fg(r):         #萬有引力公式
    return (-G*m1*m2/mag(r)**2)*norm(r)
"""
    2. 畫面設定
"""
scene=canvas(width=1200,height=800,center=vec(0,0,0),background=vec(0.6,0.8,0.8),range=2*R)
ball = sphere(radius=0.2, color = color.yellow)      #質心
ball1 = sphere(pos=vec(-R*m2/(m1+m2),0,0), radius=1, color = color.blue, make_trail=True)    #m與r成反比
ball2 = sphere(pos=vec(R*m1/(m1+m2),0,0), radius=0.3, color = color.red, make_trail=True)    
line=cylinder(pos=ball1.pos, axis=ball2.pos-ball1.pos, radius=0.05, color=color.black)    #兩球連線

ball1.v = vec(0,m2*(G/(R*(m1+m2)))**0.5,0)        #理想雙星軌跡為正圓形，推導公式並代入y方向初速度 
ball2.v = vec(0,-m1*(G/(R*(m1+m2)))**0.5,0)       #因動量守恆m1v1=m2v2，需控制系統初動量為0
"""
    3. 執行迴圈
"""
dt=0.001
while True:
    rate(1/dt)

    ball1.a=Fg(ball1.pos-ball2.pos)/m1   #球1受萬有引力
    ball1.v+=ball1.a*dt
    ball1.pos+=ball1.v*dt

    ball2.a=Fg(ball2.pos-ball1.pos)/m2    #球2受萬有引力
    ball2.v+=ball2.a*dt
    ball2.pos+=ball2.v*dt

    ball.pos=(ball1.pos*m1+ball2.pos*m2)/(m1+m2)   #質心位置
    line.pos=ball1.pos
    line.axis=ball2.pos-ball1.pos
    
    
