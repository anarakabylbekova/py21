"""
1. Создайте класс работник(Employee) который имеет обязательные переменные класса -  количество работников и прибавка к зарплате.
экземпляр класса должен иметь атрибуты name, surname, pay, email(состоящий из name и surname.@.....com)
также создайте метод экземпляр класса fullname и метод с помощью которого можно добавить прибавку к зарплате работника.
Создайте объект класса, вызовите все его методы, при создании новых объектов, должен идти подсчет количества работников.
"""


# class Employee:
#     count_employee = 0
#     salary = 500

#     def __init__(self, name, surname, pay):
#         self.name = name
#         self.surname = surname
#         self.pay = pay
#         self.email = (name + surname + '@gmail.com').lower()
#         Employee.count_employee += 1

#     def fullname(self):
#         print(self.name + self.surname)


# obj1 = Employee('John', 'Snow', 500)
# obj2 = Employee('John', 'Snow', 500)
# obj1.fullname()
# print(obj1.email)
# print(obj1.count_employee)


"""
2.Создайте класс User. 
В этом классе есть защищенный метод _create_user, который принимает email и password. 
Этот метод вызывается в публичных методах create_user и create_superuser. 
Оба метода отличаются друг от друга тем, что в методе create_user атрибут is_superuser имеет значение False, 
а в методе create_superuser - True.
Также в классе есть метод admin_login, который принимает password.
Создайте два объекта от класса User. К первому объекту примените метод create_superuser, а ко второму - create_user. 
Далее у обоих объектов вызовите метод admin_login, передав правильные пароли.
У первого объекта должно выдаваться сообщение Successfully logged in, 
а у второго - Forbidden, так как поле is_superuser у второго объекта имеет значение False. 
Также если даже is_superuser у первого объекта True, ему не удасться залогиниться, 
если он передал неправильный пароль password в метод admin_login и ему выдается сообщение: Invalid password.
"""


# class User:
#     def _create_user(self, email, password):
#         self.email = email
#         self.password = password

#     def create_user(self, email, password):
#         self.is_superuser = False
#         self._create_user(email, password)

#     def create_superuser(self, email, password):
#         self.is_superuser = True
#         self._create_user(email, password)

#     def admin_login(self, password):
#         if self.is_superuser and self.password == password:
#             print('Successfully logged in')
#         elif self.is_superuser == False:
#             print('Forbidden')
#         else:
#             print('Invalid password')

# user1 = User()
# user2 = User()

# user1.create_superuser('user1@gmail.com', 'user1')
# user2.create_user('user2@gmail.com', 'user12')

# user1.admin_login('user1')
# user2.admin_login('user2')


"""
1.Пользователи. Создайте класс с именем User. 
Создайте два атрибута first_name и last_ name, а затем еще несколько атрибутов, которые обычно хранятся в профиле пользователя. 
Напишите метод describe_user(), который выводит сводку с информацией о пользователе. 
Создайте еще один метод greet_user() для вывода персонального приветствия для пользователя. 
Напишите класс с именем Admin, наследующий от класса User из. 
Добавьте атрибут privileges для хранения списка строк вида «разрешено добавлять сообщения», 
«разрешено удалять пользователей», «разрешено банить пользователей» и т. д. 
Напишите метод show_privileges() для вывода набора привилегий администратора. 
Создайте экземпляр Admin и вызовите все методы.
"""




# class User:
   
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name 
#         self.last_name = last_name 
#         self.age = age

#     def describe_user(self):
#         print(f'{self.first_name} {self.last_name} {self.age}')

#     def greet_user(self):
#         print(f'Hello {self.first_name}')

# class Admin():
#     privileges = ['разрешено добавлять сообщения', 'разрешено удалять пользователей', 'разрешено банить пользователей']

#     def show_privileges(self):
#         print(self.show_privileges)

# admin = Admin('John', 'Snow', 50)
# admin.show_privileges()
# admin.describe_user()
# admin.greet_user()



# Ассоциация: композиция и агрегация



"""
Создайте два класса A и B. 
В обоих классах есть метод count. 
В классе A он подсчитывает, сколько гласных букв в слове, которое передается в качестве аргумента в методе count,
 а в классе B он подсчитывает количество согласных. Создайте объекты от этих классов и вызовите этот метод у каждого объекта
"""

# class A:
#     vowels = 'eyuioa'

#     def __init__(self, word):
#         self.word = word

#     def count(self):
#         counter = 0

#         for a in self.word:
#             if a in A.vowels:
#                 counter += 1
#         return counter

# class B(A):
#     def count(self):
#         counter = 0
#         for a in self.word:
#             if not a in A.vowels:
#                 counter += 1
#         return counter

# a = A('makers')
# b = B('makers')
# print(a.count())
# print(b.count())