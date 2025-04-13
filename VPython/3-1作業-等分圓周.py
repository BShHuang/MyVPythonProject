from vpython import*
"""
    1. 參數設定
"""
size=0.1     
theta=0  
R=1      
omega=2*pi  
"""
    2. 畫面設定
"""
scene=canvas(width=500,height=500,center=vector(0,0,0), background=vector(148.0/225,228.0/225,204.0/225))
ball=sphere(radius=size,color=color.blue,make_trail=True,interval=1)

v_vector = arrow(color=color.green)  #畫描述v的箭頭
v_text = label(box = False, opacity = 0, height = 25, color=color.green, text = 'v')  #產生文字標籤'v'
a_vector = arrow(color=color.red)       #畫描述a的箭頭
a_text = label(box = False, opacity = 0, height = 25, color=color.red, text = 'a')       #產生文字標籤'a'
"""
    3. 執行迴圈
"""
t=0
dt=0.001
pre_theta=theta #為了不error(pre_pretheta=pretheta要先設定)
back=False            #判斷回到原點了沒
N=5

while True:
    rate(1/dt)
    t+=dt
    '''
        畫力圖
    '''
    #取三點
    pre_pre_theta=pre_theta
    pre_theta=theta 
    theta+=omega*dt

    pre_pre_ball_pos = vector(R*cos(pre_pre_theta),R*sin(pre_pre_theta),0) #球前前時刻的位置
    pre_ball_pos = vector(R*cos(pre_theta),R*sin(pre_theta),0)                            #球前一時刻的位置
    now_ball_pos = vector(R*cos(theta),R*sin(theta),0)                                           #球現在時刻的位置
    ball.pos = pre_ball_pos                                              #（ps.上面三個可任挑，dt很小肉眼看不出來差別

    ball_v_12 = (pre_ball_pos - pre_pre_ball_pos)/dt                                                   #兩點位置決定速度 
    ball_v_23 = (now_ball_pos - pre_ball_pos)/dt       
    ball.v = ball_v_12                                                         #（ps.這兩個平均速度也可任挑，理由同上）
    ball.a=(ball_v_23 - ball_v_12)/dt                                                                    #兩速度決定加速度(需三點)

    v_text.pos = v_vector.pos + v_vector.axis*1.2 #文字標籤'v'的位置
    a_text.pos = a_vector.pos + a_vector.axis*1.2
    
    v_vector.pos = ball.pos    #將速度箭頭的位置放在球的位置
    a_vector.pos = ball.pos
    if mag(ball.v)>0:
        v_vector.axis = ball.v/mag(ball.v)*R/2    #將速度箭頭的軸方向指向速度方向，並將箭頭的長度設定為半徑的一半
        a_vector.axis = ball.a/mag(ball.a)*R/2 
    '''
        找週期並等分圓
    '''
    if back:
        plot_t=t%(T/N)                                              #將週期切成N等分，並用餘數除法設定畫圖時間點
        if plot_t+dt>=(1/N) and plot_t<(1/N): #畫圖時間判斷點
            cylinder(radius=size/50,color=color.black,axis=ball.pos) #畫細線等分圓

    #三點皆取2π的餘數，第二點最大時剛好繞一圈，此時t為週期T
    if pre_theta%(2*pi)>theta%(2*pi) and pre_theta%(2*pi)>pre_pre_theta%(2*pi):
        T=t
        print('T=',T)
        t=0
        back=True
    





    
    
