from vpython import*
"""
    1. 參數設定
"""
g = 9.8                 #重力加速度
size = 0.05                       
L = 0.5                 #彈簧原長 0.5m
k = 10                  #彈簧力常數
m = 0.1                #球質量
Fg = m*vec(0,-g,0)   #球所受重力向量
X=0.2        #調整箭頭長度
def SpringForce(r,L):
    return -k*(mag(r)-L)*r/mag(r)   #虎克定律
"""
    2. 畫面設定
"""
scene = canvas(align='left',width=600, height=600, center=vec(0, -L*0.8, 0), range=1.2*L)       #設定背景
ceiling = box(length=0.4, height=0.005, width=0.4, opacity = 0.2)            #畫天花板
ball = sphere(radius = size, pos = vec(0, -L, 0), v = vec(0, 0, 0), color=color.yellow, make_trail = True, retain = 1000, interval=1)
spring = helix(radius=0.02, thickness =0.01,pos = vec(0, 0, 0))

v_vec= arrow(shaftwidth = 0.02, color=color.green)             #畫速度箭頭
ΣF_vec= arrow(shaftwidth = 0.02, color=color.red)              #畫合力箭頭
mg_vec= arrow(shaftwidth = 0.02, color=color.yellow)       #畫重力箭頭
Fs_vec= arrow(shaftwidth = 0.02, color=color.white)           #畫彈力箭頭

v_text = label(box = False, opacity = 0, height = 25, color=color.green, text = 'v')            #在速度箭頭標示'v'
Fs_text = label(box = False, opacity = 0, height = 25, color=color.white, text = 'Fs')
mg_text = label(box = False, opacity = 0, height = 25, color=color.yellow, text = 'Fg')
ΣF_text = label(box = False, opacity = 0, height = 25, color=color.red, text = 'ΣF')

#畫E-t圖證明力學能守恆(動能+彈力位能+重力位能=定值)
gd=graph(align='right',title="Energy, green for K, red for Us, blue for Ug, black for total",width=600,height=400,xtitle="t",ytitle="energy")
f1=gcurve(color=color.blue)
f2=gcurve(color=color.red)
f3=gcurve(color=color.green)
f4=gcurve(color=color.black)
"""
    3. 執行迴圈
"""
t=0
dt = 0.001

while True:
    rate(1/dt)
    t+=dt
    
    spring.axis = ball.pos - spring.pos     
    ball.a = (Fg + SpringForce(spring.axis,L))/m              #球總共受彈力和重力
    ball.v += ball.a*dt      
    ball.pos += ball.v*dt
    '''
        畫箭頭
    '''
    v_vec.pos = ball.pos + vec(2.5*size,0,0)      #將速度箭頭設定在球的右方2.5size處
    ΣF_vec.pos = ball.pos + vec(-2.5*size,0,0)  #將合力箭頭設定在球的左方2.5size處
    mg_vec.pos = ball.pos    #將重力箭頭設定在球上
    Fs_vec.pos = ball.pos

    v_vec.axis = ball.v * X                                #設定速度箭頭，將軸方向設定為速度向量
    ΣF_vec.axis = (Fg + SpringForce(spring.axis,L)) * X  #設定合力箭頭，將軸方向設定為合力向量
    mg_vec.axis = Fg * X                                   #設定重力箭頭，將軸方向設定為重力向量
    Fs_vec.axis = SpringForce(spring.axis,L) * X

    v_text.pos = v_vec.pos + v_vec.axis*1.2
    ΣF_text.pos = ΣF_vec.pos + ΣF_vec.axis*1.2
    mg_text.pos = mg_vec.pos + mg_vec.axis*1.2
    Fs_text.pos = Fs_vec.pos + Fs_vec.axis*1.2
    '''
        畫圖表
    '''
    Ug =m*g*(ball.pos.y+L)         #預設ball.pos.y = 0處為零位面
    Us = 0.5*k*(mag(spring.axis) - L)**2
    K = 0.5*m*mag(ball.v)**2
    total=Ug+Us+K

    f1.plot(pos=(t,Ug))        
    f2.plot(pos=(t,Us))
    f3.plot(pos=(t,K))
    f4.plot(pos=(t,total))
