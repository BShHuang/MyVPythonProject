from vpython import*
"""
    1. 參數設定
"""
size = 0.5      #球的大小
"""
    2. 畫面設定
"""
scene = canvas(width=450, height=300, center=vec(2.5,0,0), background=vec(0,0,0))
#設定物件視窗的顯示畫面與背景，寬為600畫素、高為400畫素
#center為畫面中心，background為背景顏色

x = arrow(pos=vec(0,0,0), axis=vec(5,0,0), shaftwidth=0.2, color=color.green)     #畫xyz座標軸
y = arrow(pos=vec(0,0,0), axis=vec(0,5,0), shaftwidth=0.2, color=color.red)
z = arrow(pos=vec(0,0,0), axis=vec(0,0,5), shaftwidth=0.2, color=color.blue)
ball = sphere(radius=size, color=color.yellow, pos=vec(0,0,0), v=vec(0,0,0),a=vec(0,0,0))   #畫球

gd = graph(align='left',title = "x-t plot", width=300, height=200, xtitle="t", ytitle="x")     #設定函數圖
f1 = gcurve(color=color.blue)  	  #設定函數圖中線條的特性，這裡只設定顏色
gd2=graph(align='left',title="v-t plot",width=300,height=200,xtitle="t",ytitle="v")          
f2=gcurve(color=color.green)
gd3=graph(align='left',title="a-t plot",width=300,height=200,xtitle="t",ytitle="a")
f3=gcurve(color=color.red)
"""
    3. 執行迴圈
"""
dt = 0.001
t = 0.0

while t<6:
    rate(1/dt)      #迴圈執行速度
    t+=dt         

    #2秒前加速度為5，2~6秒加速度為-5
    if t<=2:
        ball.a.x=5
    else:
        ball.a.x=-5
    ball.v.x+=ball.a.x*dt    #運動
    ball.pos.x+=ball.v.x*dt
    
    if ball.v.x>0 and ball.v.x+ball.a.x*dt<=0:      #判斷轉折點(速度為正，下一瞬間速度為負)
        print('轉折點t=',t)
        print('x=',ball.pos)
        print('v=',ball.v)
    
    f1.plot(pos=(t,ball.pos.x))	#每一個迴圈畫一個點描出線條，x軸為時間，y軸為位置
    f2.plot(pos=(t,ball.v.x))
    f3.plot(pos=(t,ball.a.x))


