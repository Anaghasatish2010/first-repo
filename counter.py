import turtle

iha = turtle. Turtle()

while True:
      print("Draw a sun")
      print("Draw a shape")
      choice = input("What is your choice?")

      
           

      if choice == "Draw a shape":
            print("These are the possible shapes")
            print("Pentagon")
            print("Hexagon")
            print("Rectangle")
            choice = input("What shape do you want?")

            if choice == "Rectangle":
                 l = int(input("Enter the length"))
                 w = int(input("Enter the width"))

                 iha.forward(l)
                 iha.left(90)
                 iha.forward(w)
                 iha.left(90)
                 iha.forward(l)
                 iha.left(90)
                 iha.forward(w)
                 
            if choice == "Hexagon":
                 for side in range(6):
                      iha.forward(100)
                      iha.left(60)

            if choice == "Pentagon":
                  for side in range(5):
                   iha.forward(100)
                   iha.left(72)      

      if choice == "Draw a sun":
            iha.color("orange")
            iha.dot(100)
            while True:
                  iha.forward(100)
                  iha.backward(100)
                  iha.left(45)
                

    
        
      

