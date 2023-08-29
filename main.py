# Imports
import turtle


# Globals

# Functions

# Call Stack

# Create Screen

# Import required library

 
 
# Create screen
sc = turtle.Screen()
sc.title("Pong")
sc.bgcolor("Black")
sc.setup(width=1000, height=600)

#Left Paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=6, stretch_len=1)
left_pad.penup()
left_pad.goto(-400,0)

#Right Paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=6,stretch_len=1)
right_pad.penup()
right_pad.goto(400,0)

# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 5
ball.dy = -5

# Keybindings 
def left_paddle_up():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)

def left_paddle_down():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)

def right_paddle_up():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)

def right_paddle_down():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)


sc.listen()
sc.onkey(left_paddle_up,"z")
sc.onkey(left_paddle_down,"x")
sc.onkey(right_paddle_up,"Up")
sc.onkey(right_paddle_down,"Down")







while True:
    sc.update()
