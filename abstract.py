# class A:
#     def __init__(self):
#         self.x= 10

# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.w = 20
# class C(A):
#     def __init__(self):
#         super().__init__()
#         self.y = 40

# class D(B,C):
#     def __init__(self):
#         super().__init__()

# d1 = D()

# print(d1.x , d1.y , d1.w)


class Shape():
    def __init__(self,color):
         self.color = color
        

    def area(self):
            pass

    def get_color(self):
         return self.color
    
class Circle(Shape):
     def __init__(self, radius, color):
          super().__init__(color)
          self.radius = radius

class Rectangle(Shape):
     def __init__(self, width, height, color):
          super().__init__(color)
          self.width = width
          self.height = height

c1 = Circle("red", 10)
r1 = Rectangle(2,3,"blue")

print(f"Area {c1.area()}")
print(f"Area {r1.area()}")
    
   
    
          