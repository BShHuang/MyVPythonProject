'''
Pendulum wave的特色：
多個擺錘釋放一段時間之後，一定會再次呈現所有擺錘連成一線的現象。
這代表在這段時間內，擺長最長的擺錘擺N次，第二長的擺N-1次，以此類推
'''
from vpython import *
"""
    1. 參數設定
"""
g = 9.8                    #重力加速度9.8m/s^2
theta = 10*pi/180        #初始擺角設定
k = 100000          #彈力常數
m = 1.0                  #擺錘的質量
n = 12                    #單擺個數
d = 0.1                   #每個擺錘之間的間隔為d公尺 
size = d/3.5         #擺錘圓球半徑的大小
T0=1          #最長擺錘週期
N=1            #釋放擺錘經過N*T0時間後再度全連成一線
L = [g*(((N*T0/(N+i))/2*pi)**2) for i in range(n)]      #每一根擺繩的長度(單擺公式L=((2pi/T)**2)*g，T=N*T0/(N+i))

def SpringForce(r,L):     #擺錘所受的彈力
    return - k*(mag(r)-L) * r / mag(r)
"""
    2. 畫面設定
"""
scene = canvas(width=600, height=800,center = vec(0, -L[int(n/2)]/2-d, d*n/2+0.15), range=0.9)     
ceiling = box(pos=vec(0,0,(n-1)*d/2), length=0.03, height=0.001, width=(n-1)*d*1.01, color=vec(0.7,0.7,0.7))    
timer = label(pos=vec(5*d,2*d,d*n/2), box = False, height = 20, color=color.yellow)     #在物件視窗用label做計時器

ball = []      #產生空白的list，稍後從迴圈將擺錘一個一個放進去
string = []    #產生空白的list，稍後從迴圈將擺繩一根一根放進去
for i in range(0,n,1):     #用range指令產生list，i為0~11，放入擺錘和擺繩的初始位置
    ball.append(sphere(pos=vec(L[i]*sin(theta), -L[i]*cos(theta), d*i), v=vec(0,0,0), radius=size, color=color.yellow))
    string.append(cylinder(pos=vec(0,0,d*i), color=vec(0.7,0.7,0.7), radius=0.001))
    #用append指令將物件一個一個擺入list中，i為range這個list的元素
"""
    3. 執行迴圈
"""
dt = 0.001    #時間間隔
t = 0         #初始時間
while True:
    rate(1/dt)
    t = t+dt            #累計時間
    Ts = t % 60         #計算「秒 sec」
    Tm = int( t/60 )    #計算「分 min」
    timer.text = str('Timer : \n') + str('%1.0f'%Tm) + str(' min ') + str('%1.2f '%Ts) + str(' sec')

    a = []    #產生一個空白的list，稍後計算每一個擺錘的加速度，並放入此list中
    for j in range(0,n,1):
        string[j].axis = ball[j].pos - string[j].pos                    #計算每一根擺繩的軸方向
        a.append(vec(0,-g,0)+SpringForce(string[j].axis, L[j])/m)    #計算每一個擺錘的加速度
        ball[j].v += a[j]*dt            #計算每一個擺錘的速度
        ball[j].pos += ball[j].v*dt     #計算每一個擺錘的位置
