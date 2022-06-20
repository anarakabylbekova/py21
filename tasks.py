"""
8. Создайте класс Password, экземеплярами класса являются пароли в виде строк. 
У класса должен быть метод validate для валидации пароля:
- пароль должен быть минимум 8 символов, но меньше 15
- пароль должен содержать цифры
- пароль должен содержать буквы
- пароль должен содержать хотя бы один из символов:
    '@', '#', '&', '$', '%', '!', '~', '*'

если одно из условий не выполнено, выводите кастомное исключение, 
если же все условия выполнены метод validate должен возвращать строку: 'Ваш пароль сохранен'.

Также переопределите метод __str__, чтобы при попытке распечатать
сам пароль, вам выдавалась строка из звездочек,
к примеру пароль - 'joe@123456'
в терминале выйдет - **********
"""

# class Password:
#     def __init__(self, password):
#         self.password = password

#     def __str__(self):
#         return len(self.password) * '*'
    
#     def validate(self):
#         list_ = ['@', '#', '&', '$', '%', '!', '~', '*']
#         if not len(self.password) >= 8 and not len(self.password) <=15:
#             raise Exception('Пароль неправильной длины')
#         elif self.password.isalpha():
#             raise Exception('Добавьте цифры!')
#         elif self.password.isdigit():
#             raise Exception('Добавьте буквы')
#         elif not any ([i in list_ for i in self.password]):
#             raise Exception('Добавьте символ')
#         else:
#             return 'Все хорошо!'

    

# password1 = Password('hello123!')
# print(password1.validate())



"""
10. Создайте класс Character с помощью которого можно создавать героев для игры. 
Экземпляры класса должны иметь аттрибут name. У класса должна быть переменная power_list, в которой хранится словарь:
power_list = { 'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }

Класс должен иметь методы:
give_weapon - выбирает случайное оружие из списка

give_role - выбирает случайную роль из списка, к примеру:
["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]

give_powers, передавая силу и значение можно менять power_list для определенного героя, к примеру:
char1.give_powers('ловкость', 5)
увеличит ловкость вашего героя.

Создайте три разных дочерьних класса от класса Character - Elf, Orc, DragonBorn, 
дайте каждому из классов уникальный метод и добавьте уникальные аттрибуты экземпляра класса,наследуя __init__ от Character. 
Создайте несколько героев от этих классов и вызовите их методы и методы родительского класса Character. 
"""

# import random

# class Character:
#     power_list = { 'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }

#     def __init__(self, name):
#         self.name = name

#     def give_weapon(self):
#         weapon_list = ['1', '2', '3', '4', '5']
#         return random.choice(weapon_list)

#     def give_role(self):
#         role_list = ["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]
#         return random.choice(role_list)
    
#     def get_powers(self, key, value):
#         self.power_list[key] = value

# class Elf(Character):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age

#     def get_age(self):
#         return self.age

# obj1 = Character('obj1')
# print(obj1.give_weapon)


# class Song:
    
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def show_title(self):
#         return f'Название этой песни {self.title}'

#     def show_author(self):
#         return f'Автор этой песни {self.author}'

#     def show_year(self):
#         return f'Эта песня вышла в {self.year} году'

# song = Song('Happy', 'Pharrell Williams', 2013)
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())


# class Circle:
#     color = 'Синий'
#     pi = 3.14

#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         return (self.radius **2) * 3.14

# circle = Circle(2)
# circle.color = 'красный'
# print(circle.get_area())
# print(circle.color)

# class BankAccount:
    
#     def __init__(self):
#         self.balance = 0

#     def withdraw(self, amount):
#         self.balance -= amount
#         return f'Ваш баланс {self.balance} сом'
    
#     def deposit(self, amount):
#         self.balance += amount
#         return f'Ваш баланс {self.balance} сом'

# account = BankAccount()
# print(account.deposit(1000))
# print(account.withdraw(500))


# class Taxi:

#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km

#     def get_total_cost(self, km):
#         new_cost = (km * self.cost_km) + self.cost
#         return f'Такси {self.name}, стоимость поездки: {new_cost}'
    
# taxi1 = Taxi('Namba', 17, 17)
# taxi2 = Taxi('Yandex', 12, 15)
# taxi3 = Taxi('Jorgo', 23, 10)
# print(taxi1.get_total_cost(10))
# print(taxi2.get_total_cost(6))
# print(taxi3.get_total_cost(14))



# class Phone:
#     def __init__(self, name, last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone

#     def get_info(self):
#         return f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}'

# contact = Phone('John', 'Snow', '+996707707707')
# print(contact.get_info())




    
