from vpython import*


scene=canvas(width=600,height=400,center=vector(2.5,0,0),background=vector(0,0,0))
x=arrow(pos=vector(0,0,0),axis=vector(1,0,0),color=color.green)
y=arrow(pos=vector(0,0,0),axis=vector(0,1,0),color=color.red)
z=arrow(pos=vector(0,0,0),axis=vector(0,0,1),color=color.blue)
ball=sphere(radius=0.1,color=color.orange,pos=vector(0,0,0),v=vector(-2,0,0),a=vector(3,0,0))
#設定動畫和球


gd=graph(title="x-t plot",width=600,height=400,xtitle="t",ytitle="x")
f1=gcurve(color=color.blue)
gd2=graph(title="v-t plot",width=600,height=400,xtitle="t",ytitle="v")
f2=gcurve(color=color.red)
gd3=graph(title="a-t plot",width=600,height=400,xtitle="t",ytitle="a")
f3=gcurve(color=color.green)
#設定圖表

t=0
dt=0.001
#設定初始值

while t<=3:
    rate(1/dt)
    t=t+dt
    ball.pos.x=ball.pos.x+ball.v.x*dt
    ball.v.x=ball.v.x+ball.a.x*dt
    #主程式

    f1.plot(pos=(t,ball.pos.x))
    f2.plot(pos=(t,ball.v.x))
    f3.plot(pos=(t,ball.a.x))
    #設定函數圖的畫面
    
    if ball.v.x<0 and ball.v.x+ball.a.x*dt>=0:
        print(t)
        print(ball.pos)
        print(ball.v)
    #折返點為v<0到v>0(因「==」要成立的條件判斷極其嚴苛，必須到小數點以下十幾位都要一樣，判斷才會成立，所以以範圍dt的方式寫條件判斷)
        
    if t<3 and t+dt>=3:
        print(ball.pos.x)
    #同理球在3秒「瞬間」也用範圍條件
