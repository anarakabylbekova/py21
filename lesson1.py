# Введение в ООП

# ООП - Объектно-ориентированное программирование - парадигма (набор правил написания) программирования, в котором все основывается на 2 ключевых понятиях класс и объект


# Класс - Дает общую характеристику, которую будут использовать их объекты
# Объект - экземпляр класса 

# class GetInfo:
#     name = 'John'  # Атрибут класса

#     def get_name(self, age):
#         print(f'Привет тебя зовут {self.name}, тебе {age} лет')

# obj1 = GetInfo()
# obj1.name = 'Nick'
# obj2 = GetInfo()
# print(obj1.name)
# print(obj2.name)
# print(dir(obj1))

# obj1.get_name(18)
# obj2.get_name(30)


# class Animal():
#     def __init__(self, name, animal_type):
#         self.name = name  # атрибут экземпляра класса
#         self.animal_type = animal_type
    
#     def get_info(self):
#         return f'Имя объекта - {self.name} и тип - {self.animal_type}'

# cat = Animal('Barsik', 'cat')
# print(cat.name)
# dog = Animal('Rex', 'dog')
# print(dog.name)

# print(cat.get_info())
# print(dog.get_info())


# class Person:
#     is_alive = True

#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age

#     def get_info(self):
#         return f'{self.name}, {self.last_name}, {self.is_alive}'

#     def birthday(self): 
#         past_age = self.age
#         self.age += 1
#         print('С днем рождения!!!')
#         print(f'Тебе было {past_age} и стало {self.age}')

# obj1 = Person('John', 'Snow', 31)
# print(obj1.get_info())
# obj1.birthday()



# class Bank:
#     total = 0

#     def get_summ(self):
#         print(self.total)

#     def add_summ(self, summ):
#         self.total += summ
#         self.get_summ()

#     def min_sum(self, summ):
#         if self.total - summ < 0:
#             raise Exception('Недостаточно средств!')
#         self.total -= summ
#         self.get_summ()

# client1 = Bank()
# client1.get_summ()
# client1.add_summ(100)
# client1.get_summ()
# client1.min_sum(1000)
# client1.get_summ()


# Example1:

# class Dog:
#     owner = 'Ann'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f'{self.name}, {self.age}'

#     def bark(self):
#         print('Gav-gav')

#     def dog_info(self):
#         return f'This is {self.name}, he is {self.age} years old.'

#     def birthday(self, cake):
#         self.age += 1
#         self.cake = cake
#         return f'{self.name} is {self.age} now'

#     def friends(self, friend):
#         self.friend = friend
#         friend.friend = self




# dog1 = Dog('Rex', 2)
# dog2 = Dog('Hanna', 3)
# dog1.friends(dog2)
# print(dog1.friend)
# print(dog2.friend.age)

# dog1.bark()
# dog2.bark()
# print(dog1)
# print(dog2)
# print(dog1.dog_info())
# print(dog2.dog_info())
# print(dog1.birthday('Choco'))
# print(dog2.birthday('Vanila'))
# print(dog1.cake)
# print(dog2.cake)
# print(dog1.age)
# print(dog1.name)
# print(dog1.age)
# print(dog1.owner)




# Example2:

# class Rectangle:
#     default_color = 'red'

#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
    
#     def area(self):
#         return self.width * self.length


# rec1 = Rectangle(4, 6)
# rec2 = Rectangle(2, 7)
# rec2.default_color = 'yellow'
# print(rec1.area())
# print(rec1.width)
# print(rec2.area())
# print(rec1.default_color)
# print(rec2.default_color)


# Example3:

# class Car:
#     car_count = 0

#     def __init__(self):
#         Car.car_count += 1

# car1 = Car()
# print(Car.car_count)
# car2 = Car()
# car3 = Car()
# car4 = Car()
# print(Car.car_count)



# Task1
# import random

# class Sniper:

#     def __init__(self, name):
#         self.name = name
#         self.health = 100

#     def shoot(self, sniper):
#         sniper.health -= 20

# sniper1 = Sniper('Ben')
# sniper2 = Sniper('Tom')

# choices = (sniper1, sniper2)

# while True:
#     shooter = random.choice(choices)
#     if shooter == sniper1:
#         shot = sniper2
#     else:
#         shot = sniper1
#     shooter.shoot(shot)
#     print (f'Shooter {shooter.name} is shooting, {shot.name} has {shot.health} health points')

#     if sniper1.health == 0:
#         print(f'{sniper1.name} is dead. {sniper2.name} won!!!')
#         break
#     elif sniper2.health == 0:
#         print(f'{sniper2.name} is dead. {sniper1.name} won!!!')
#         break
#     else:
#         continue


# Task 2

# class Hogwarts:
    
#     faculties_qualities = {'courage': 'Gryffindor', 
#                             'intelligence': 'Ravenclow', 
#                             'justice': 'Hufflepuff', 
#                             'ambition': 'Slytherin'}
    
#     def __init__(self, courage, intelligence, justice, ambition):
#         self.courage = courage
#         self.intelligence = intelligence
#         self.justice = justice
#         self.ambition = ambition
#         self.qualities_dictionary = locals()
#         # print(self.qualities_dictionary)

#     def sorting_hat(self):
#         dictionary = {val: key for key, val in self.qualities_dictionary.items() if type (val) == int}
#         # print(dictionary)
#         maximum_point = max(dictionary.keys())
#         # print(maximum_point)
#         maximum_quality = dictionary[maximum_point]
#         # print(maximum_quality)
#         self.faculty = Hogwarts.faculties_qualities[maximum_quality]
#         print(f'{self.faculty}!!!')

# student1 = Hogwarts(courage=5, intelligence=8, justice=3, ambition=9)
# student1.sorting_hat()
# student2 = Hogwarts(courage=8, intelligence=6, justice=1, ambition=0)
# student2.sorting_hat()
# student3 = Hogwarts(courage=4, intelligence=7, justice=3, ambition=2)
# student3.sorting_hat()
# student4 = Hogwarts(courage=3, intelligence=5, justice=9, ambition=1)
# student4.sorting_hat()






