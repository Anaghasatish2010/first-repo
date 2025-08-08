
import turtle
import random
player_speed = 1

window = turtle.Screen()
window.tracer(0)


player = turtle.Turtle()
player.color("green")
player.shape("turtle")
player.penup()

fruit = turtle.Turtle()
fruit.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
fruit.shape("circle")
fruit.penup()

def teleport_fruit():
  fruit.setx(random.randint(-200,200))
  fruit.sety(random.randint(-200,200))
  fruit.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))


def go_up():
  if player.heading() !=270:
    player.setheading(90)

def go_left():
  if player.heading() !=0:
    player.setheading(180)
  
  
def go_right():
  if player.heading() !=180:
    player.setheading(0)
 

def go_down():
  if player.heading() !=90:
    player.setheading(270)
 
  
window.onkey(go_up, "Up")
window.onkey(go_left, "Left")
window.onkey(go_right, "Right")
window.onkey(go_down, "Down")
window.listen()

game_is_running = True 
teleport_fruit()
while game_is_running:
  window.update()
  player.forward(player_speed)
  
  if player.distance(fruit) < 20:
    teleport_fruit()
    player_speed = player_speed + 0.5
    
  if player.xcor() < -200:
      game_is_running = False
      
  if player.xcor() > 200:
      game_is_running = False
      
  if player.ycor() < -200:
      game_is_running = False
      
  if player.ycor() > 200:
      game_is_running = False

turtle.done()


    
  
       



