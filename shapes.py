# import turtle
# number_of_sides = 6

# bob = turtle.Turtle()
 
# for side in range(number_of_sides):
#     bob.forward(100)
#     bob.left(360/number_of_sides)

# import turtle
# number_of_sides = input("how many sides")
# number_of_sides = int(number_of_sides)

# bob = turtle.Turtle()
 
# for side in range(number_of_sides):
#     bob.forward(100)
#     bob.left(360/number_of_sides)

# if 5==6:
#  print("This is true")

# age = 24 

# if age >= 18:
#     print("this person is old enough")

# if age < 18:
#     print("this person is too young")

# age = 14

# if age >= 18:
#     print("this person is old enough")
# else:
#     print("this person is too young")

# counter = 0
# while True:
#     print(counter)
#     counter = counter + 1

# counter = 0
# is_running = True

# while is_running:
#     print(counter)
#     counter = counter + 1
#     if counter >= 50:
#      is_running = False

# import turtle

# bob = turtle.Turtle()

# print("possible shapes are:")
# print("Circle")
# print("Triangle")
# print("Square")
# choice = input("What shape do you want ")

# if choice == "Circle":
#     bob.circle(50)

# if choice == "Triangle":
#     for side in range(3):
#         bob.forward(100)
#         bob.left(120)

# if choice == "Square":
#     for side in range(4):
#         bob.forward(100)
#         bob.left(90)

# import turtle

# bob = turtle.Turtle()

# while True:
#  print("possible shapes are:")
#  print("Circle")
#  print("Triangle")
#  print("Square")
#  choice = input("What shape do you want ")

#  if choice == "Circle":
#     bob.circle(50)

#  if choice == "Triangle":
#     for side in range(3):
#         bob.forward(100)
#         bob.left(120)

#  if choice == "Square":
#     for side in range(4):
#         bob.forward(100)
#         bob.left(90)

import turtle

bob = turtle.Turtle()

while True:
 print("What do you want to do")
 print("Change color")
 print("Draw a shape")
 choice = input("What is your choice?")

 if choice == "Change color":
     color = input("what color do you want")
     bob.color(color)

 if choice == "Draw a shape":
  print("possible shapes are:")
  print("Circle")
  print("Triangle")
  print("Square")
  choice = input("What shape do you want ")

 if choice == "Circle":
     bob.circle(50)

 if choice == "Triangle":
    for side in range(3):
        bob.forward(100)
        bob.left(120)

 if choice == "Square":
    for side in range(4):
        bob.forward(100)
        bob.left(90)





