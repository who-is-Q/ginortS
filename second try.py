import turtle
import math


def drawLine(angle,length):
    turtle.left(angle)
    turtle.forward(length)


def drawStar(length):
    #draw the first line in the star
    drawLine(36,length)
    #make a turns and finish the rest of lines
    for n in range(4):
        drawLine(144,length)


def drawCrescent(radius,color):
    #give color and begin defining the boundery of the filled color part
    turtle.fillcolor(color)
    turtle.begin_fill()
    #draw a a
    turtle.circle(radius,-180)
    #make a trun and draw another
    turtle.right(30)
    turtle.circle(2*radius/(3**0.5),240)
    #finish defining the boundery of the filled color part,and fill the color
    turtle.end_fill()
    turtle.hideturtle()
    
def drawQatarFlag():
    #draw a rectangular
    for i in range(2):
        turtle.forward(250)
        turtle.left(90)
        turtle.forward(130)
        turtle.left(90)
    #draw the colored part and fill maroon
    turtle.forward(50)
    turtle.fillcolor("maroon")
    turtle.begin_fill()
    turtle.left(math.atan(65/(9*20))/math.pi*180)
    turtle.forward((20**2+(65/9)**2)**0.5)
    #outline the colred part
    for n in range(8):
        turtle.left(180-2*math.atan(65/(9*20))/math.pi*180)
        turtle.forward((20**2+(65/9)**2)**0.5)
        turtle.right(180-2*math.atan(65/(9*20))/math.pi*180)
        turtle.forward((20**2+(65/9)**2)**0.5)
    turtle.left(180-2*math.atan(65/(9*20))/math.pi*180)
    turtle.forward((20**2+(65/9)**2)**0.5)
    turtle.right(180-math.atan(65/(9*20))/math.pi*180)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(130)
    turtle.right(90)
    turtle.forward(200)
    turtle.end_fill()
    turtle.hideturtle()

def drawUSFlag():
    #adjust the direction of the turtle
    turtle.right(90)
    #initialize color filling of the stripes
    for n in range(6):
        turtle.fillcolor("maroon")
        turtle.begin_fill()
    #outline the stripes part
        for n in range(2):
            turtle.forward(10)
            turtle.right(90)
            turtle.forward(250)
            turtle.right(90)
        turtle.end_fill()
        turtle.forward(20)
    turtle.fillcolor("maroon")
    turtle.begin_fill()
    for n in range(2):
            turtle.forward(10)
            turtle.right(90)
            turtle.forward(250)
            turtle.right(90)
    turtle.end_fill()
    #go to the initial place of the blue part
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(130)
    #initialize the color filling of the blue part
    turtle.fillcolor("blue")
    turtle.begin_fill()
    #outline the blue part
    for n in range(2):
        turtle.right(90)
        turtle.forward(110)
        turtle.right(90)
        turtle.forward(70)
    turtle.end_fill()
    #adjust the direction and positon of pen to draw stars
    turtle.right(90)
    turtle.penup()
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()
    #draw stars
    turtle.color("white")
    turtle.fillcolor("white")
    for n in range(2):
        #draw the first line of the stars
        for n in range(5):
            turtle.begin_fill()
            drawStar(10)
            turtle.end_fill()
            turtle.penup()
            turtle.left(108)
            turtle.forward(18)
            turtle.pendown()
        turtle.begin_fill()
        drawStar(10)
        turtle.end_fill()
        turtle.penup()
        turtle.left(18)
        turtle.forward(15)
        turtle.right(90)
        turtle.forward(80)
        turtle.left(180)
        turtle.pendown()
        #draw the second line of the stars
        for n in range(5):
            turtle.begin_fill()
            drawStar(10)
            turtle.end_fill()
            turtle.penup()
            turtle.left(108)
            turtle.forward(18)
            turtle.pendown()
        turtle.penup()
        turtle.right(90)
        turtle.forward(15)
        turtle.right(90)
        turtle.forward(100)
        turtle.left(180)
        turtle.pendown()
    #move the pen to where the last line of stars start
    for n in range(5):
            turtle.begin_fill()
            drawStar(10)
            turtle.end_fill()
            turtle.penup()
            turtle.left(108)
            turtle.forward(18)
            turtle.pendown()
    #draw the last line of stars
    turtle.fillcolor("white")
    turtle.begin_fill()
    drawStar(10)
    turtle.end_fill()
    

def drawPAKFlag():
    #draw the outline of the flag
    for n in range(2):
        turtle.right(90)
        turtle.forward(130)
        turtle.right(90)
        turtle.forward(250)
    #draw and fill the green part of the flag
    turtle.fillcolor("green")
    turtle.begin_fill()
    for n in range(2):
        turtle.right(90)
        turtle.forward(130)
        turtle.right(90)
        turtle.forward(188)
    turtle.end_fill()
    #adjust the position of turtle to where the star starts
    turtle.penup()
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.pendown()
    #draw the star
    turtle.color("white")
    turtle.fillcolor("white")
    turtle.begin_fill()
    drawStar(25)
    turtle.end_fill()
    #adjust the position of turtle to where the crescent starts
    turtle.penup()
    turtle.left(36*3)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    #draw the crescent
    turtle.pendown()
    turtle.left(90)
    drawCrescent(30,"white")    
    turtle.hideturtle()




#draw the long stripe on the Korean flag
def Line1():
    turtle.fillcolor("black")
    turtle.begin_fill()
    for n in range(2):
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(5)
        turtle.left(90)
    turtle.end_fill()
    #move to the position where next stike might be
    turtle.penup()
    turtle.left(90)
    turtle.forward(8)
    turtle.right(90)
    turtle.pendown()

#draw the second kind of stripe on the Korean flag
def Line2():
    #draw the first part of the stripe
    turtle.fillcolor("black")
    turtle.begin_fill()
    for n in range(2):
        turtle.forward(18)
        turtle.left(90)
        turtle.forward(5)
        turtle.left(90)
    turtle.end_fill()
    #adjust turtle to where the second part of the stripe begins
    turtle.penup()
    turtle.forward(22)
    turtle.pendown()
    #draw the second part of the stripe
    turtle.begin_fill()
    for n in range(2):
        turtle.forward(18)
        turtle.left(90)
        turtle.forward(5)
        turtle.left(90)
    turtle.end_fill()
    #move to the position next strike might be
    turtle.penup()
    turtle.left(180)
    turtle.forward(22)
    turtle.right(90)
    turtle.forward(8)
    turtle.right(90)
    turtle.pendown()

def gotoNext(length):
    turtle.penup()
    turtle.right(90)
    turtle.forward(39)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(43)
    turtle.forward(length)
    turtle.right(45)
    turtle.pendown()

def drawSKFlag():
    #draw the outline of the flag
    for n in range(2):
        turtle.forward(250)
        turtle.left(90)
        turtle.forward(130)
        turtle.left(90)
    turtle.penup()
    #adjust the position of turtle to where the blue circle starts
    turtle.forward(165)
    turtle.left(90)
    turtle.forward(65)
    turtle.pendown()
    #draw the blue circle
    turtle.color("darkblue")
    turtle.fillcolor("darkblue")
    turtle.begin_fill()
    turtle.circle(40,360)
    turtle.end_fill()
    #draw the red part of the circle
    turtle.color("maroon")
    turtle.fillcolor("maroon")
    turtle.begin_fill()
    turtle.circle(20,180)
    turtle.circle(-20,180)
    turtle.circle(-40,180)
    turtle.end_fill()
    #adjust to where upper left stripes are
    turtle.color("black")
    turtle.penup()
    turtle.left(180)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(45)
    turtle.color("black")
    #draw the upper left group of stripes
    Line2()
    Line1()
    Line2()
    #adjust to where lower left stripes are
    gotoNext(18)
    #draw the lower left group of stripes
    Line2()
    Line2()
    Line2()
    #adjust to where lower right stripes are
    gotoNext(95) 
    #draw the lower right group of stripes
    Line1()
    Line2()
    Line1()
    #adjust to where upper left stripes are 
    gotoNext(18)
    #draw the upper right group of stripes
    Line1()
    Line1()
    Line1()

def drawAllFlags():
    drawQatarFlag()
    #move to where the US flag starts
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(130)
    turtle.right(90)
    drawUSFlag()
    #move to where Pakistan flag starts
    turtle.color("black")
    turtle.penup()
    turtle.left(108)
    turtle.goto(0,0)
    turtle.pendown()
    drawPAKFlag()
    #move to where South Korea flag starts
    turtle.right(30)
    turtle.color("black")
    turtle.penup()
    turtle.goto(0,0)
    turtle.right(90)
    turtle.forward(130)
    turtle.left(90)
    turtle.pendown()
    drawSKFlag()
    


turtle.tracer(0)
drawAllFlags()



