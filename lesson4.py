# class MyStr(str):
#     def __str__(self):
#         return super().__str__ () + ' world'


# obj1 = MyStr('hello')
# # print(dir(obj1))
# print(obj1)



# class A:
#     name = 'John'

#     def __init__(self,name, last_name):
#         self.name = name
#         self.last_name = last_name

#     def hello(self):
#         return('hello')
        

# class B(A):
#     def __init__(self,name, last_name, age):
#         super().__init__(name, last_name)
#         self.age = age

#     def hello(self):
#         return super().hello() + ' hello world'

# a = A('Nick', 'Snow2')
# b = B('John','Snow', 6)
# # print(dir(b))
# print(a.hello())
# print(b.hello())

# class Game:
#     __level = 0

#     def play_game(self, hours):
#         if hours > 2:
#             self.__level += 1
    
#     # def get_level(self):
#     #     return self.__level

#     # def set_level(self, value):
#     #     self.__level = value

#     @property
#     def level(self):
#         return self.__level

#     @level.setter
#     def level(self, value):
#         self.__level = value

# john = Game()
# john.play_game(3)
# # print(john.get_level())
# john.play_game(3)
# # print(john.get_level())
# # print(john._Game__level)
# john.level = 100
# print(john.level)


# class Soda:
    
#     def __init__(self, a):
#         if isinstance(a, str):
#             self.a = a
    
# obj1 = Soda('hello world')
# obj2 = Soda(4)
# print(obj1.a)
# print(obj2.a)


# class KgToPounds:
    
#     def init(self, kg):
#         self.__kg = kg

#     def set_kg(self, new_kg):
#         self.__kg = new_kg
    
#     def get_kg(self):
#         return self.__kg

#     @property
#     def kg(self):
#         return self.__kg
    
#     @kg.setter
#     def kg(self, value):
#         self.__kg = value






