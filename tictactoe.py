import turtle
window = turtle.Screen()
window.tracer(0)
window.setup(600,600)
grid = turtle.Turtle()

def move_to(x,y):
  turtle.setposition(x,y)

window.onclick(move_to)

def draw_line(start_x, start_y, end_x, end_y):
  grid.penup()
  grid.setposition(start_x, start_y)
  grid.pendown()
  grid.setposition(end_x, end_y)
  
def draw_grid():
  draw_line(-300, 100, 300, 100)
  draw_line(-300, -100, 300, -100)
  draw_line(-100, 300, -100, -300)
  draw_line(100, 300, 100, -300)
  
draw_grid()
player = turtle.Turtle()

def draw_x():
  player.color("black")
  
  player.left(45)
  for _ in range(4):
    player.forward(140)
    player.forward(-140)
    player.left(90)
  
  player.right(45)


def draw_o():
  player.color("black")
  player.dot(150)
  player.color("white")
  player.dot(130)
  


window.is_crosses = True


def floor(value):
  return ((value + 700) // 200) * 200 - 600
  
def draw(x, y):
  x = floor(x)
  y = floor(y)
  
  player.penup()
  player.setposition(x, y)
  player.pendown()
  
  if window.is_crosses:
    draw_x()
    window.is_crosses = False
  
  else:
    draw_o()
    window.is_crosses = True
    
  window.update()
  
window.onclick(draw)
turtle.done()