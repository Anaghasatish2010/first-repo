class SampleClass:
    x = 0
    def __init__(self):
        self.y = 10

    def change_object(self,new_x,new_y):
        print(self.y)
        self.y = new_y

        print("class:",self.__class__)
        print("class attribute x: " , self.__class__.x)

        self.__class__.x = new_x

    @classmethod
    def change_class(cls):
        print("Class Attribute X", cls.x)
        cls.x = 1000

    @staticmethod
    def auxilary_method():
        print("inside static method")

SampleClass.auxilary_method()
obj = SampleClass()
obj.auxilary_method()
