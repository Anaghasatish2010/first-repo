import turtle
import random
window = turtle.Screen()

window.setup(600, 400)
window.tracer(0)

ball = turtle.Turtle()
ball.left(random.randint(0, 360))
ball.shape("circle")
ball.penup()


left_paddle = turtle.Turtle()
left_paddle.shape("square")
# left_paddle.shapesize(2, 0.5)
left_paddle.penup()
left_paddle.setx(-270)

right_paddle = turtle.Turtle()
right_paddle.shape("square")
# right_paddle.shapesize(2, 0.5)
right_paddle.penup()
right_paddle.setx(270)

def left_paddle_up():
  left_paddle.sety(left_paddle.ycor() + 3)
  
def left_paddle_down():
  left_paddle.sety(left_paddle.ycor() - 3)
  
def right_paddle_up():
  right_paddle.sety(right_paddle.ycor() + 3)
  
def right_paddle_down():
  right_paddle.sety(right_paddle.ycor() - 3)
  
window.onkey(left_paddle_up, "w")
window.onkey(left_paddle_down, "s")
window.onkey(right_paddle_up, "Up")
window.onkey(right_paddle_down, "Down")
window.listen()

ball_speed = 1
right_score = 0
left_score = 0

while True:
  window.update()
  ball.forward(ball_speed)
  
  if ball.distance(right_paddle) < 30:
    ball.setheading(random.randint(160, 200) - ball.heading())
    ball_speed += 1
    
  if ball.distance(left_paddle) < 30:
    ball.setheading(random.randint(160, 200) - ball.heading())
    ball_speed += 1
    

  if ball.ycor() > window.window_height() / 2:
    ball.setheading(-ball.heading())
    
  if ball.ycor() < -window.window_height() / 2:
    ball.setheading(-ball.heading())
    
  if ball.xcor() > window.window_width() / 2:
    ball.goto(0, 0)
    left_score += 1
    ball_speed = 1
    
  if ball.xcor() < -window.window_width() / 2:
    ball.goto(0, 0)
    right_score += 1
    ball_speed = 1


w
