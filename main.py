
import turtle
import time



# Object Creation
# Drawing screen and game elemets
 
# Create screen
Screen = turtle.Screen()
Screen.title("Pong")
Screen.bgcolor("Black")
Screen.setup(width=1000, height=600)

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
ball.speed(400)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2.25
ball.dy = -2.25

# Score Display
score_display = turtle.Turtle()
score_display.color("White")
score_display.penup()
score_display.hideturtle()
score_display.goto(0,260)
score_display.write("Player 1: 0 Player 2: 0", align="center",font=("Arial",24,"normal"))

# Keybindings 
#Creating keybinds and there assosiate rules and interactions
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


Screen.listen()
Screen.onkey(left_paddle_up,"z")
Screen.onkey(left_paddle_down,"x")
Screen.onkey(right_paddle_up,"Up")
Screen.onkey(right_paddle_down,"Down")

# Game Rules
game_over = False
winner = None
points = {
    "Player1": 0,
    "Player2": 0
}
game_rules = {
    "Max Points": 3,
    "Ball_Speed": 3
}

# Call Stack
while True:
    Screen.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    Screen.update()

    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 500:
        ball.goto(0, 0)
        ball.dy *= -1
        
    if  ball.xcor() < -500:
        ball.goto(0, 0)
        ball.dy *= -1

    if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < right_pad.ycor()+40 and ball.ycor() > right_pad.ycor()-40):
        ball.setx(360)
        ball.dx*=-1
        
    if (ball.xcor()<-360 and ball.xcor()>-370) and (ball.ycor()<left_pad.ycor()+40 and ball.ycor()>left_pad.ycor()-40):
        ball.setx(-360)
        ball.dx*=-1
        
        
        
