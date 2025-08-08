
# class TV:
#     def __init__(self):
#         self.status = "off"
#         self.channel = 1
#         self.volume = 50

#     def __str__(self):
#         return f"TV Status:{self.status} , channel:{self.channel} , volume:{self.volume}"
    
# tv1 = TV()
# print(tv1.volume)
# print(tv1.channel)
# tv1.volume = 190
# tv1.channel = 18
# print(tv1)

# adding single undersocre just tells other programmers not to change it


# class TV:
#     def __init__(self):
#         self._status = "off"
#         self._channel = 1
#         self._volume = 50

#     def __str__(self):
#         return f"TV Status:{self._status} , channel:{self._channel} , volume:{self._volume}"
    
# tv1 = TV()
# print(tv1._volume)
# print(tv1._channel)
# tv1._volume = 200
# tv1._channel = -1
# print(tv1)

# adding double undersocre

class TV:
    def __init__(self):
        self.__status = "off"
        self.__channel = 1
        self.__volume = 50
        
    def __str__(self):
        return f"TV Status:{self.__status} , channel:{self.__channel} , volume:{self.__volume}"
    

tv1 = TV()
print(tv1.__dir__())
print(tv1._TV__volume)
print(tv1._TV__channel)
tv1._TV__channel = -1
tv1._TV__volume = 200

print(tv1)






    
    