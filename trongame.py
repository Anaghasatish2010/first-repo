import turtle
import time

previous_positions = []

window = turtle.Screen()
window.setup(600, 600)

player = turtle.Turtle()
player.penup()
player.color('red')

def turn_right():
    if player.heading() !=(180):
          player.setheading(0)

def turn_left():
    if player.heading() !=(0):
          player.setheading(180)

def turn_up():
    if player.heading() !=(90):
          player.setheading(270)

def turn_down():
    if player.heading() !=(270):
         player.setheading(90)

window.onkey(turn_right, "Right")
window.onkey(turn_left, "Left")
window.onkey(turn_up, "Up")
window.onkey(turn_down, "Down")

while True:
     for side in previous_positions:
          print(player.distance(side))
     print(previous_positions)
     previous_positions.append(player.pos())
     player.forward(20)
     player.stamp()

     time.sleep(0.1)



               