from vpython import*
"""
    1. 參數設定
"""
G=6.67*10**(-11)
M=6*10**24
m=1000
Re=6.4*10**6
R=5*Re
V0=((G*M)/R)**0.5
sum_area=0

def Fg(r):
    return -(G*M*m/(mag(r)**2))*norm(r)
"""
    2. 畫面設定
"""
scene = canvas(align = 'left',  width=800, height=300, background=vec(0.6,0.8,0.8))
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth)
meteor = sphere(radius=0.1*Re,color=color.red, make_trail=True)
meteor2 = sphere(radius=0.1*Re,color=color.yellow, make_trail=True)#用來證明K3L

meteor.pos=vec(R,0,0)
pre_meteor_pos = vec(0,0,0)
meteor.v=vec(0,0.7*V0,0)
meteor2.pos=vec(1.5*R,0,0)#用來證明K3L
pre_meteor2_pos = vec(0,0,0)
meteor2.v=vec(0,0.7*V0,0)


v_arrow = arrow(pos=meteor.pos,axis=vec(0,0,0),shaftwidth=0.4*meteor.radius ,color = color.red)
a_arrow = arrow(pos=meteor.pos,axis=vec(0,0,0),shaftwidth=0.4*meteor.radius ,color = color.white)
aT_arrow = arrow(pos=meteor.pos,axis=vec(0,0,0),shaftwidth=0.6*meteor.radius ,color = color.black)
aN_arrow = arrow(pos=meteor.pos,axis=vec(0,0,0),shaftwidth=0.6*meteor.radius ,color = color.blue)

#證明力學能守恆的圖表
gd = graph(align='left',width=400,height=400,title='K+U=E', xtitle='t', ytitle='E(red) , K(black) , U(green)')
f1 = gcurve(color=color.red)
f2 = gcurve(color=color.black)
f3 = gcurve(color=color.green)

"""
    3. 執行迴圈
"""
T=0#周期
T2=0#用來證明K3L
t=0
dt=1

while True:
    rate(5000)
    T+=dt
    T2+=dt#用來證明K3L
    t+=dt

    pre_pre_meteor_pos = pre_meteor_pos
    pre_meteor_pos = vector(meteor.pos.x , meteor.pos.y, meteor.pos.z)
    pre_pre_meteor2_pos = pre_meteor2_pos#用來證明K3L
    pre_meteor2_pos = vector(meteor2.pos.x , meteor2.pos.y, meteor2.pos.z)
    
    meteor.a=Fg(meteor.pos-earth.pos)/m
    meteor.v+=meteor.a*dt
    meteor.pos+=meteor.v*dt
    meteor2.a=Fg(meteor2.pos-earth.pos)/m#用來證明K3L
    meteor2.v+=meteor2.a*dt
    meteor2.pos+=meteor2.v*dt

    #畫速度箭頭
    v_arrow.pos = meteor.pos
    v_arrow.axis = meteor.v*2*10**3 #乘2*10**3  #為了讓動畫的速度向量顯著
    a_arrow.pos = meteor.pos
    a_arrow.axis = meteor.a*5*10**6 #同理
    aT_arrow.pos = meteor.pos
    aT_arrow.axis = dot(meteor.a,meteor.v)*(norm(meteor.v)/mag(meteor.v))*5*10**6
    aN_arrow.pos = meteor.pos
    aN_arrow.axis = (mag(cross(meteor.a,meteor.v))/mag(meteor.v))*cross(norm(meteor.v),vector(0,0,-1))*5*10**6

    #找端點、長軸a、短軸b、周期
    if pre_meteor_pos.x > pre_pre_meteor_pos.x and pre_meteor_pos.x > meteor.pos.x and t>30000:
        A1=meteor.pos.x
        a=A1-A2
        b=B1-B2
        print('a=',a,', b=',b)
        print('T=',T)
        print('k=',(0.5*a)**3/(T**2))#用來證明K3L
        T=0
    if pre_meteor_pos.x < pre_pre_meteor_pos.x and pre_meteor_pos.x < meteor.pos.x : 
       A2=meteor.pos.x
    if pre_meteor_pos.y > pre_pre_meteor_pos.y and pre_meteor_pos.y > meteor.pos.y :
       B1=meteor.pos.y
    if pre_meteor_pos.y < pre_pre_meteor_pos.y and pre_meteor_pos.y < meteor.pos.y : 
       B2=meteor.pos.y

    #用來證明K3L 
    if pre_meteor2_pos.x > pre_pre_meteor2_pos.x and pre_meteor2_pos.x > meteor2.pos.x and t>50000:
        AA1=meteor2.pos.x
        aa=AA1-AA2
        bb=BB1-BB2
        print('T2=',T2)
        print('k2=',(0.5*aa)**3/(T2**2))
        T2=0
    if pre_meteor2_pos.x < pre_pre_meteor2_pos.x and pre_meteor2_pos.x < meteor2.pos.x : 
       AA2=meteor2.pos.x
    if pre_meteor2_pos.y > pre_pre_meteor2_pos.y and pre_meteor2_pos.y > meteor2.pos.y :
       BB1=meteor2.pos.y
    if pre_meteor2_pos.y < pre_pre_meteor2_pos.y and pre_meteor2_pos.y < meteor2.pos.y : 
       BB2=meteor2.pos.y
       
##    #證明K2L(不能同時證明力學能守恆，需先註解掉，因「t=0」E-t圖會不斷從t=0畫)
##    a = mag(meteor.pos-earth.pos)  #定義三角形的三邊長
##    b = mag(earth.pos-pre_meteor_pos)
##    c = mag(pre_meteor_pos-meteor.pos)
##    s =(a+b+c)/2      
##    area =(s*(s-a)*(s-b)*(s-c))**0.5
##    sum_area += area            #累加每dt時刻內的面積，計算總面積
##    if t >= 2785 :
##        print ('sum_area=',sum_area)
##        t = 0
##        sum_area = 0 
##        cylinder(pos=earth.pos, axis=meteor.pos-earth.pos, radius=0.01*Re, color=color.black)  #每2785秒將地球與衛星之間連線繪圖

    #證明力學能守恆
    meteorK = 0.5*m*(mag(meteor.v))**2 #動能
    meteorU = -G*M*m/mag(meteor.pos-earth.pos)#位能
    meteorE = meteorK+meteorU

    f1.plot(pos=(t,meteorE))
    f2.plot(pos=(t,meteorK))
    f3.plot(pos=(t,meteorU))


