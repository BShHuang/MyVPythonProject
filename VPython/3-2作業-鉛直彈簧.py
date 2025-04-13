from vpython import*
g = 9.8              
size = 0.05                       
L = 0.5                 #彈簧原長 0.5m
k = 10                  
m = 0.1                 
Fg = m*vector(0,-g,0)
X=0.2

scene = canvas(width=600, height=600, center=vector(0, -L*0.8, 0), range=1.2*L)
ceiling = box(length=0.4, height=0.005, width=0.4, opacity = 0.2)
ball = sphere(radius = size,  color=color.yellow, make_trail = True, retain = 1000, interval=1)
spring = helix(radius=0.02, thickness =0.01)


def SpringForce(r,L):
    return -k*(mag(r)-L)*r/mag(r)

ball.pos = vector(0, -L, 0)     
ball.v = vector(0, 0, 0)        
spring.pos = vector(0, 0, 0)

v_vector = arrow(shaftwidth = 0.02, color=color.green)
ΣF_vector = arrow(shaftwidth = 0.02, color=color.red)
mg_vector = arrow(shaftwidth = 0.02, color=color.yellow)
Fs_vector = arrow(shaftwidth = 0.02, color=color.white)

v_text = label(box = False, opacity = 0, height = 25, color=color.green, text = 'v')
Fs_text = label(box = False, opacity = 0, height = 25, color=color.white, text = 'Fs')
mg_text = label(box = False, opacity = 0, height = 25, color=color.yellow, text = 'Fg')
ΣF_text = label(box = False, opacity = 0, height = 25, color=color.red, text = 'ΣF')

gd=graph(title="Energy, green for K, red for Us, blue for Ug, black for total",width=600,height=400,xtitle="t",ytitle="energy")
f1=gcurve(color=color.blue)
f2=gcurve(color=color.red)
f3=gcurve(color=color.green)
f4=gcurve(color=color.black)

t=0
dt = 0.001

while True:
    rate(1/dt)
    t+=dt
    
    spring.axis = ball.pos - spring.pos     
    ball.a = (Fg + SpringForce(spring.axis,L))/m
    ball.v += ball.a*dt      
    ball.pos += ball.v*dt

    v_vector.pos = ball.pos + vector(2.5*size,0,0)      #將速度箭頭設定在球的右方2.5size處
    ΣF_vector.pos = ball.pos + vector(-2.5*size,0,0)  #將合力箭頭設定在球的左方2.5size處
    mg_vector.pos = ball.pos    #將重力箭頭設定在球上
    Fs_vector.pos = ball.pos

    v_vector.axis = ball.v * X                                #設定速度箭頭，將軸方向設定為速度向量
    ΣF_vector.axis = (Fg + SpringForce(spring.axis,L)) * X  #設定合力箭頭，將軸方向設定為合力向量
    mg_vector.axis = Fg * X                                   #設定重力箭頭，將軸方向設定為重力向量
    Fs_vector.axis = SpringForce(spring.axis,L) * X

    v_text.pos = v_vector.pos + v_vector.axis*1.2
    ΣF_text.pos = ΣF_vector.pos + ΣF_vector.axis*1.2
    mg_text.pos = mg_vector.pos + mg_vector.axis*1.2
    Fs_text.pos = Fs_vector.pos + Fs_vector.axis*1.2
  
    Ug =m * g * (ball.pos.y+L)
    Us = 0.5 * k * (mag(spring.axis) - L)**2
    K = 0.5 * m * mag(ball.v)**2
    total=Ug+Us+K

    f1.plot(pos=(t,Ug))
    f2.plot(pos=(t,Us))
    f3.plot(pos=(t,K))
    f4.plot(pos=(t,total))
