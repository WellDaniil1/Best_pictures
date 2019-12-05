# Case 1
# Task 1

import turtle

turtle.hideturtle()

def triangle(a,b,x,y,anglemain,angle,angle1,color):
    turtle.up()
    turtle.goto(a,b)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.left(anglemain)
    turtle.forward(x)
    turtle.left(180 - angle)
    turtle.forward(y)
    turtle.left(180 - angle1)
    turtle.goto(a,b)
    turtle.up()
    turtle.end_fill()
    turtle.left(angle + angle1 - anglemain)

def square(x,y,a,angle,color):
    turtle.up()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.left(angle)
    for i in range (4):
        turtle.left(90)
        turtle.forward(a)
    turtle.end_fill()
    turtle.goto(x,y)
    turtle.left(180 - angle)

def rhombus(a,b,x,anglemain,angle,color):
    turtle.up()
    turtle.goto(a,b)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.left(anglemain)
    for i in range(2):
        turtle.forward(x)
        turtle.left(angle)
        turtle.forward(x)
        turtle.left(180 - angle)
    turtle.end_fill()
    turtle.goto(a,b)
    turtle.right(anglemain)

triangle(0,300,50,50,30,60,60,'orange')
triangle(0,300,50,50,90,60,60,'orange')
triangle(0,300,50,50,150,60,60,'orange')

triangle(0,300,50,50,-30,60,60,'orange')
triangle(0,300,50,50,-90,60,60,'orange')
triangle(0,300,50,50,-150,60,60,'orange')

square(-300,300,30,0,'blue')
square(-270,330,30,0,'blue')
rhombus(-285,300,21,45,90,'yellow')
rhombus(-285,300,58,255,30,'yellow')
