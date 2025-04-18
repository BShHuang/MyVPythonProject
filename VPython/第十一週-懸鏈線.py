from vpython import*
import numpy as np
"""
    1. 參數設定
"""
N = 50		#質點個數
g = 9.8		#重力加速度
size, m, k, d = 0.016, 0.1/N, N*1000, 2/N    #球大小、質點質量、各力常數、間距
"""
    2. 畫面設定
"""
scene = canvas(width=1200, height = 600, center = vec(d*N/2*0.9, 0, 0)) 
balls = [sphere(radius=size, color=color.yellow) for i in range(N)]    #畫50個球
springs = [helix(radius = size/2, thickness = size/5) for i in range(N-1)]  #畫49個彈簧

ball_pos, ball_v, ball_g = np.zeros((N, 3)), np.zeros((N,3)), np.zeros((N,3))
#以array建立初位置、初速度、重力加速度，全為0的N列3行的陣列

for i in range(N):
    ball_pos[i][0] = d*i*0.9 #將球沿x方向的初位置，沿axis=0(向下)擺入pos array，並使兩端點距離為0.9倍繩子全長
    ball_pos[i][1] = d*i*0.2
    ball_g[i][1] = -g        #將重力加速度陣列的第2行改為-9.8，表示每個球在y方向受到的重力場
"""
    3. 執行迴圈
"""
t, dt = 0, 0.0001
T=50*dt  #加速動畫執行(每執行50個迴圈畫一張圖)

while True:
    rate(1/dt)
    t += dt 
    
    spring_axis = ball_pos[1:] - ball_pos[:-1]        #每個彈簧的軸方向((2~N)-(1~N-1))
    b = np.sum(spring_axis**2, axis = 1)**0.5         #每個彈簧的長度(xyz平方和開根號，沿axis=1(向右)加)
    spring_axis_unit = spring_axis / b[:, np.newaxis] #每個彈簧軸方向的單位向量(b需擴充至二維(N列1行)才能除)
    fs = - k * (spring_axis - d*spring_axis_unit)     #每個彈簧的作用力
    fs[b<=d] = 0                                      #彈簧長度小於原長設為零，表示繩子的鬆弛狀態
    
    ball_v[1:-1] += (fs[:-1] - fs[1:])/m*dt + ball_g[1:-1]*dt - 5*ball_v[1:-1]*dt    #計算第二個~倒數第二個球的速度
                                                                                                                  #空氣阻力(消除震動)
    ball_pos += ball_v *dt                            #計算球的位置

    if t%T<T and t%T+dt>T:    #加快畫圖速度
        for i in range(N):        #畫球
            balls[i].pos = vec(ball_pos[i][0], ball_pos[i][1], ball_pos[i][2])
        for i in range(N-1):      #畫彈簧
            springs[i].pos = balls[i].pos
            springs[i].axis = balls[i+1].pos - balls[i].pos
            
    #證明三力平衡必共點
    if t>5:
        G_total = np.sum(ball_g*m, axis=0)                 #質心所受重力
        CM = np.sum(ball_pos*m, axis=0) / (m*N)    #質心位置

        arrow_G=arrow(pos=vec(*CM),axis=vec(*G_total)*0.3,color=color.white)         #畫出重力方向箭頭
        arrow_T1=arrow(pos=balls[0].pos,axis=vec(*fs[0])*0.3,color=color.red)             #畫出繩子頭端受力方向箭頭
        arrow_T2=arrow(pos=balls[-1].pos,axis=-vec(*fs[-1])*0.3,color=color.green)    #畫出繩子尾端受力方向箭頭

        #三力的延長線
        line_T1=cylinder(radius=size/10, color=color.green,pos = arrow_T1.pos,axis = vec(*fs[0]).norm()*-1.5)  
        line_T2=cylinder(radius=size/10, color=color.green,pos = arrow_T2.pos,axis = vec(*fs[-1]).norm()*1.5)
        line_G=cylinder(radius=size/10, color=color.green,pos = arrow_G.pos,axis = vec(*G_total).norm()*1)
    
