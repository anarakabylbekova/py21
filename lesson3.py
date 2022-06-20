# Инкапсуляция. getter/setter методы.

# Инкапсуляция:
    # 1) Объединение всех свойств и методов в одну капсулу или же класс
    # 2) Ограничение доступа к методам и атрибутам, т.е. сокрытие данных от внешнего воздействия

# 3 модификации доступа:
    # public - публичный - данные доступны всем
    # _protected - защищенный - данные доступны как внутри класса, так и у дочерних классов
    # __private - приватный - данные доступны только классу, в котором он находится

## @property   # декоратор - это функция, которая расширяет фукнционал другой функции за счет себя


# class A:
#     name = 'John'
#     _age = 30
#     __last_name = 'Snow'


#     def get_name(self):
#         return self.name
    
#     def _get_age(self):
#         return self._age
    
#     def __get_last_name(self):
#         return(self.__last_name)


# class B(A):
#     def get_info(self):
#         print(self.name)
#         print(self._age)
#         print(self._A__last_name)

# obj2 = B()
# obj2.get_info()


# obj1 = A()
# print(obj1.name)
# print(obj1._age)
# print(obj1._A__last_name)
# print(obj1.get_name())
# print(obj1._get_age())
# print(obj1._A__get_last_name())



# class Game:
#     __level = 0

#     @property   # getter
#     def level(self):
#         return self.__level

#     @level.setter  # setter
#     def level(self, value):
#         self.__level = value

#     # def get_level(self):
#     #     return self.__level
    
#     # def set_level(self, value):
#     #     self.__level = value


# obj1 = Game()
# # print(obj1.get_level())
# # obj1.set_level(5)
# # print(obj1.get_level())
# print(obj1.level)
# obj1.level = 5
# print(obj1.level)


# class Student:

#     def __init__(self, name):
#         self.name = name
#         self.knowledge = 0

#     def read_book(self):
#         self.__add_point(5)

#     def __add_point(self, point):
#         self.knowledge += point

# obj1 = Student('Nick')
# print(obj1.knowledge)
# # obj1.add_point(100)
# obj1.read_book()
# print(obj1.knowledge)







