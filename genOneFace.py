from turtle import Screen, Turtle
from PIL import Image
from createGaussianNumbers import *
import os


# Get Face
def face(r, turtle):
    turtle.penup()
    # Set pointer to middle of the canvas
    turtle.setpos(0, -r)
    turtle.pendown()
    turtle.circle(r)
    turtle.penup()


def eye(col, r, turtle):
    turtle.pendown()
    turtle.fillcolor(col)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.penup()


def twoEyes(bigCol, smallCol, r1, r2, turtle, p1=-25, p2=32):
    turtle.setpos(-p1, p2)
    eye(bigCol, r1, turtle)
    turtle.setpos(-p1, p2)
    eye(smallCol, r2, turtle)
    turtle.setpos(p1, p2)
    eye(bigCol, r1, turtle)
    turtle.setpos(p1, p2)
    eye(smallCol, r2, turtle)


def nose(r, turtle, p1=0, p2=0):
    turtle.setpos(p1, p2)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(-5, -r)
    turtle.goto(5, -r)
    turtle.goto(p1, p2)
    turtle.end_fill()
    turtle.shape("triangle")


def mouse(r, turtle):
    turtle.penup()
    turtle.setpos(0, -32)
    turtle.setheading(180)
    turtle.pendown()
    turtle.circle(-r, 90)
    turtle.penup()
    turtle.setpos(0, -32)
    turtle.setheading(0)
    turtle.pendown()
    turtle.circle(r, 90)


def oneFace(*pars):
    assert len(pars) == 11
    turtle = Turtle()
    # Hide the pointer to be able to draw quick
    turtle.hideturtle()
    turtle.speed(0)
    facer, eyer1, eyer2, eyep1, eyep2, noser, nosep1, nosep2, mouser, bigCol, smallCol = pars
    face(facer, turtle)
    twoEyes(bigCol, smallCol, eyer1, eyer2, turtle, eyep1, eyep2)
    nose(noser, turtle, nosep1, nosep2)
    mouse(mouser, turtle)
    # Clear for next turtles
    turtle.clear()


def setEnv():
    # Set the window size
    # ADD 2 FOR BOREDER !
    WIDTH, HEIGHT = 130, 130
    # Init the screen to be able to change default size
    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    # set the pointer position
    screen.setworldcoordinates(-64, -64, 64, 64)
    return screen


def saveImgAndConvert(i, screen):
    cv = screen.getcanvas()
    fn = str(i) + ".ps"
    cv.postscript(file=fn, colormode='color')
    image = Image.open(fn)
    image.save(str(i) + '.jpeg', 'jpeg')
    print(str(i) + 'is done')
    os.remove(fn)


def main():
    # Set the window size
    WIDTH, HEIGHT = 128, 128
    # Init the screen to be able to change default size
    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    # set the pointer position
    screen.setworldcoordinates(-64, -64, 64, 64)
    turtle = Turtle()
    # Hide the pointer to be able to draw quick
    turtle.hideturtle()
    face(64, turtle)
    twoEyes('white', 'black', 8, 4, turtle)
    nose(8, turtle)
    mouse(12, turtle)
    # screen.exitonclick()
    cv = screen.getcanvas()
    cv.postscript(file="test.ps", colormode='color')


if __name__ == "__main__":
    main()
