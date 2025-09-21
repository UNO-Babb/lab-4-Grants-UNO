#TurtleGraphics.py
#Name: Grant Schaeffer
#Date: 9/21/25
#Assignment: Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(phil, sides):
    for s in range(sides):
        phil.forward(60)
        phil.right(366/sides)
        
        
def fillCorner(robin, corner):
    drawSquare(robin, 120)
    if corner == 1:
        robin.begin_fill()
        drawSquare(robin,60)
        robin.end_fill()
    elif corner == 2:
        robin.forward(60)
        robin.begin_fill()
        drawSquare(robin,60)
        robin.end_fill()
    elif corner == 3:
        robin.right(90)
        robin.forward(60)
        robin.left(90)
        robin.begin_fill()
        drawSquare(robin,60)
        robin.end_fill()
    elif corner == 4:
        robin.penup()
        robin.forward(60)
        robin.right(90)
        robin.forward(60)
        robin.left(90)
        robin.pendown()
        robin.begin_fill()
        drawSquare(robin,60)
        robin.end_fill()
        
def squaresInSquares(charles, num)
    for n in range(num):
        drawSquare(charles, num)
        charles.penup()
        charles.forward(10)
        charles.right(90)
        charles.forward(10)
        charles.left(90)
        charles.pendown()

    

def main():
    myTurtle = turtle.Turtle()

    #drawSquare(myTurtle, 100)
    #drawPolygon(myTurtle, 6)
    # drawPolygon(myTurtle, 8)

    #fillCorner(myTurtle, 1) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares
