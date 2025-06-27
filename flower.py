# import turtle

# flower = turtle.Turtle()
# flower.penup()

# def draw_flower(number_of_petals, petal_colour,middle_colour):
#    for petal in range(number_of_petals):
#       flower.color(petal_colour)
#       flower.forward(25)
#       flower.dot(50)
#       flower.backward(25)
#       flower.left(360/number_of_petals)    

#    flower.color(middle_colour)
#    flower.dot(50)

# flower.backward(150)
# draw_flower(5, "red", "yellow")
# flower.forward(75)
# draw_flower(3, "violet", "purple")
# flower.forward(75)
# draw_flower(6, "blue", "pink")
# flower.forward(75) 
# draw_flower(4, "lime", "black")

# import turtle

# window = turtle.Screen()

# bob = turtle.Turtle()

# def turn_left():
#     bob.left(10)

# def turn_right():
#     bob.right(10)

# def go_forward():
#     bob.forward(10)

# def change_pen_state():
#     if bob.isdown():
#         bob.penup()
#     else:
#         bob.pendown()

# def color_red():
#     bob.color("red")

# def color_blue():
#     bob.color("blue")

# def color_green():
#     bob.color("green")
        

# window.onkey(turn_left, "Left")
# window.onkey(turn_right, "Right")
# window.onkey(go_forward, "Up")
# window.onkey(change_pen_state, "space")
# window.onkey(color_red, "1")
# window.onkey(color_blue, "2")
# window.onkey(color_green, "3")
# window.listen()

# while True:
#     bob.forward(1)

# import turtle

# window = turtle.Screen()

# bob = turtle.Turtle()

# def goto(x,y):
#     bob.setx(x)
#     bob.sety(y)

# window.onclick(goto)

# bob.forward(1)

import turtle

window = turtle.Screen()

bob = turtle.Turtle()
bob.penup()

def draw_flower(petal_color, middle_color, number_of_petals):
    bob.color(petal_color)
    for petal in range(number_of_petals):
        bob.forward(10)
        bob.dot(20)
        bob.backward(10)
        bob.left(360/ number_of_petals)
    bob.color(middle_color)
    bob.dot(20)

def draw_flower_in_position(x,y):
    bob.setx(x)
    bob.sety(y)

    draw_flower("red", "yellow", 5)

window.onclick(draw_flower_in_position)

bob.forward(1)

turtle.done()









