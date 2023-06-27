import turtle

# Creating Screen
screen = turtle.getscreen()
turtle.hideturtle()
screen.title("Paddle Game")
screen.bgcolor("blue")
screen.screensize(canvwidth=600, canvheight=600)

# Creating Paddle
paddle = turtle.Turtle()
paddle.speed(0) 
paddle.shape("square")
paddle.color("white")
paddle.shapesize(1, 4)
paddle.penup() 
paddle.goto(0, -275)

# Creating Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 100) 
paddle.speed(0) 

# Created Actions
def paddle_right():
    x = paddle.xcor()        # Get the x position of paddle
    if x < 225:
        paddle.setx(x+20)    # increment the x position by 20

def paddle_left():
    x = paddle.xcor()        # Get the x position of paddle
    if x > -225:
        paddle.setx(x-20)    # decrement the x position by 20

# Keyboard Control


done = False

# Display Screen
while not done:
   screen.update()
   paddle_left()

