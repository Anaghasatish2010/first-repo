# list_of_names = ["Bob", "Kevin", "Michael", "George", "Vlad"]

# for name in["Bob", "Kevin", "Michael", "George", "Vlad"]:
#     print(name)

# list_of_names = ["Bob", "Kevin", "Michael", "George", "Vlad"]
# print(list_of_names)

# for name in["Bob", "Kevin", "Michael", "George", "Vlad"]:
#     print(name)

# list_of_names = ["Bob", "Kevin", "Michael", "George", "Vlad"]


# for name in["Bob", "Kevin", "Michael", "George", "Vlad"]:
#     if name[0] == "B":
#         print(name)
#         print("this name starts with a b")

# list_of_names = ["Bob", "Kevin", "Michael", "George", "Vlad"]


# for name in["Bob", "Vevin", "Michael", "George", "Vlad"]:
#     if name[0] == "V":
#         print(name)
#         print("this name starts with a v")

# import turtle

# list_of_color = ["blue", "pink", "purple", "red"]

# bob = turtle.Turtle()
# bob.shape("turtle")

# counter = 0
# while True:
#     bob.color(list_of_color[counter])
#     bob.left(180)

#     counter = counter+1
#     if counter >= len(list_of_color):
#         counter = 0

import turtle

list_of_color = ["blue", "pink", "purple", "red"]

bob = turtle.Turtle()
bob.shape("turtle")

while True:
    for color in list_of_color:
        print(color)
        bob.color(color)
        bob.left(180)
   

