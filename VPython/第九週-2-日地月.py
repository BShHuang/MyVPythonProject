from vpython import *
"""
    1. 參數設定
"""
#真實數據
G = 6.67e-11                 #萬有引力常數
m1 = 1.9891e30          #太陽質量
m2 = 5.9742e24          #地球質量
m3 = 7.342e22             #月球質量
Rsun=6.955e8              #太陽半徑
Rearth=6.3728e6        #地球半徑
Rmoon=1.7371e6       #月亮半徑
R_12 = 1.496e11         #太陽與地球距離
R_23 = 3.84399e8      #地球與月亮距離
v2 = (G*m1/R_12)**0.5   #地球以圓周運動繞太陽(靜止)的速率
v3 = (G*m2/R_23)**0.5   #月球以圓周運動繞地球(靜止)的速率

def Fg(r,M1,M2):      #萬有引力公式
    return -(G*M1*M2/(mag(r)**2))*norm(r)
"""
    2. 畫面設定
"""
scene = canvas(width=1200, height=800, center=vec(0,0,0),background=vec(0.6,0.8,0.8),range=7*R_23)
ball1 = sphere(pos=vec(0,0,0), radius=20*Rsun, color = color.yellow, make_trail=True)        #太陽(放大20倍不然看不到)
ball2 = sphere(pos=vec(R_12,0,0), radius=20*Rearth, texture=textures.earth, make_trail=True)     #地球
ball3 = sphere(pos=vec(R_12+R_23,0,0), radius=20*Rmoon,  color = color.red, make_trail=True)    #月亮

ball1.v = vec(0,0,0)        #太陽靜止
ball2.v = vec(0,v2,0)      #從太陽靜止座標系看地球的相對速度
ball3.v = vec(0,v2+v3,0)   #從太陽靜止座標系看月球的相對速度

pre_m1m2_pos = vec(0,0,0)    #三點紀錄法
pre_m2m3_pos = vec(0,0,0)
r_12=vec(0,0,0)
r_23=vec(0,0,0)
"""
    3. 執行迴圈
"""
T1=0
T2=0
dt = 100

while True:
    rate(10000)
    T1+=dt
    T2+=dt
    scene.center = ball2.pos       #以地球為畫面中心
    
    Fg_12=Fg(ball2.pos-ball1.pos,m1,m2)       # 地球太陽的力
    Fg_23=Fg(ball3.pos-ball2.pos,m2,m3)      # 月球地球的力
    Fg_13=Fg(ball3.pos-ball1.pos,m1,m3)      # 月球太陽的力

    ball2.a=(Fg_12-Fg_23)/m2    #地球受太陽與月球的萬有引力，注意地球與月球的力是「-」
    ball2.v += ball2.a*dt
    ball2.pos += ball2.v*dt

    ball3.a=(Fg_23+Fg_13)/m3   #月球受太陽與地球的萬有引力
    ball3.v += ball3.a*dt
    ball3.pos += ball3.v*dt

    #三點紀錄法
    pre_pre_m1m2_pos = pre_m1m2_pos
    pre_m1m2_pos = vec(r_12.x , r_12.y,r_12.z)        #「有設初始值先寫」

    pre_pre_m2m3_pos = pre_m2m3_pos
    pre_m2m3_pos =vec(r_23.x , r_23.y,r_23.z)

    r_12=norm(ball2.pos-ball1.pos)               #「變數後寫」
    r_23=norm(ball3.pos-ball2.pos)
    r_13=norm(ball3.pos-ball1.pos)
    
    if pre_m1m2_pos.x > pre_pre_m1m2_pos.x and pre_m1m2_pos.x > r_12.x:      #地球繞太陽一圈
        Te=T1/86400     #以天為單位
        print('Te=','%1.2f'%Te)
        T1=0

    #月亮實際週期是兩次日地月連線(滿月)的時間，繞超過一圈，所以看相對位置判斷繞一圈
    if mag(pre_m1m2_pos-pre_m2m3_pos) > mag(pre_pre_m1m2_pos-pre_pre_m2m3_pos)\
       and mag(pre_m1m2_pos-pre_m2m3_pos) >mag(r_12-r_23) :
        Tm=T2/86400
        print ('Tm=' , '%1.2f'%Tm)
        T2=0
    
