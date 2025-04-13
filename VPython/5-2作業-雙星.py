from vpython import*
"""
    1. 參數設定
"""
G = 6.67
m1 = 10
m2 = 3
R = 10
def Fg(r):
    return (-G*m1*m2/mag(r)**2)*norm(r)
"""
    2. 畫面設定
"""
scene=canvas(width=1200,height=800,center=vec(0,0,0),background=vec(0.6,0.8,0.8),range=2*R)

ball1 = sphere(pos=vector(-R*m2/(m1+m2),0,0), radius=1, color = color.blue, make_trail=True)#m1r1=m2r2
ball2 = sphere(pos=vector(R*m1/(m1+m2),0,0), radius=0.3, color = color.red, make_trail=True)
ball1.v = vector(0,m2*(G/(R*(m1+m2)))**0.5,0) #因動量守恆m1v1=m2v2，需控制系統初動量為0
ball2.v = vector(0,-m1*(G/(R*(m1+m2)))**0.5,0)

"""
    3. 執行迴圈
"""
t=0
dt=0.001
while True:
    rate(1/dt)
    t+=dt

    ball1.a=Fg(ball1.pos-ball2.pos)/m1
    ball1.v+=ball1.a*dt
    ball1.pos+=ball1.v*dt

    ball2.a=Fg(ball2.pos-ball1.pos)/m2
    ball2.v+=ball2.a*dt
    ball2.pos+=ball2.v*dt

    
