r1 = 200
r2 = 200  
m1 = 40
m2 = 40
a1 = PI/2
a2 = PI/2
a1_v = 0 
a2_v = 0

px2 = -1
py2 = -1

cx = 0
cy = 0

g =  1

canvas = 0

def setup():
    global canvas
    global cx
    global cy

    size(900,600,P2D)
    
    cx = width/2
    cy = 200
    canvas = createGraphics(width,height)
    canvas.beginDraw()
    canvas.background(255)
    canvas.endDraw()

def draw():
    global canvas
    global a1
    global a2
    global px2
    global py2
    global a1_v
    global a2_v

    
    a1_a = (((-g*((2*m1)+m2))*sin(a1))-(m2*g*sin(a1-(2*a2)))-(2*sin(a1-a2)*m2*((a2_v*a2_v*r2)+(a1_v*a1_v*r1*cos(a1-a2))))) / (r1*((2*m1)+m2-(m2*cos((2*a1)-(2*a2)))))  
    a2_a = (2*sin(a1-a2)*((a1_v*a1_v*r1*(m1+m2))+(g*(m1+m2)*cos(a1))+(a2_v*a2_v*r2*m2*cos(a1-a2)))) / (r2*((2*m1)+m2-(m2*cos((2*a1)-(2*a2)))))
    
    
    image(canvas,0,0)
    stroke(0)
    strokeWeight(2)
    
    translate(cx,cy)
    
    x1 = r1 * sin(a1)
    y1 = r1 * cos(a1)
    
    x2 = x1 + (r2 * sin(a2))
    y2 = y1 + (r2 * cos(a2))
    
    
    
    line(0,0, x1,y1)
    fill(0)
    ellipse(x1,y1,m1,m1)
    
    line(x1,y1,x2,y2)
    fill(0)
    ellipse(x2,y2,m2,m2)
    
    a1_v += a1_a
    a2_v += a2_a
    
    a1 += a1_v
    a2 += a2_v
    
    #a1_v *= 0.9999
    #a2_v *=0.9999

    canvas.beginDraw()
    canvas.translate(cx,cy)
    canvas.strokeWeight(1)
    canvas.stroke(0)
    if frameCount > 1:
        canvas.line(px2,py2,x2,y2)
    canvas.endDraw()
    
    px2 = x2
    py2 = y2
