from turtle import Turtle, Screen
from random import seed, randint

seed()

DELAY = 100  # milliseconds

# setup the output window
picSize = (400, 600)
playGround = Screen()
playGround.screensize(*picSize)

# setup the turtles
bob = Turtle(shape='turtle', visible=False)
bob.penup()
bob.color('red')
bob.speed('slow')

jeff = Turtle(shape='turtle', visible=False)
jeff.penup()
jeff.color('blue')
jeff.speed('normal')

x_quadrant = -picSize[0] // 2, picSize[0] // 2
y_quadrant = -picSize[1] // 2, picSize[1] // 2

# find random positions for the turtles
jeff_xy = randint(*x_quadrant), randint(*y_quadrant)
bob_xy = randint(*x_quadrant), randint(*y_quadrant)

# find a point to move bob to and rotate towards its target location
bobNew_xy = randint(*x_quadrant), randint(*y_quadrant)
bob.setheading(bob.towards(bobNew_xy))

# place the turtles and show them
jeff.setpos(jeff_xy)
jeff.showturtle()
jeff.pendown()

bob.setpos(bob_xy)
bob.showturtle()
bob.pendown()

# bob's motion is in a straight line
def moveStraight():
    bob.fd(bob.speed())
    playGround.ontimer(moveStraight, DELAY)

# jeff's motion is towards bob
def moveToward():
    if bob.position() != jeff.position():
        jeff.setheading(jeff.towards(bob))
        jeff.fd(jeff.speed())
    playGround.ontimer(moveToward, DELAY)

moveStraight()
moveToward()

playGround.exitonclick()