# Основные принципы ООП: Наследование

# class A:
#     a = 5

#     def get_a(self):
#         print(self.a)

# class B(A):
#     pass

# obj_a = A()
# print(obj_a.a)
# obj_b = B()
# print(obj_b.a)
# obj_b.get_a()


# class Person:
#     def __init__(self, name, last_name, pol):
#         self.name = name
#         self.last_name = last_name
#         self.pol = pol
    
#     def __str__(self):
#         return self.name

#     def display_name(self):
#         print(f'Name: {self.name}')


# class Employee(Person):

#     def __init__(self, name, last_name, pol, age):
#         # Person().__init__(name, last_name, pol) 
#         super().__init__(name, last_name, pol)  
#         self.age = age  

#     def work(self):
#         print('Я работаю')

# # person = Person('John')
# # print(person)
# employee = Employee('John', 'Snow', 'm', 6)
# print(employee.name)


# class A:
#     a = 5

#     def info(self):
#         # print('Hello')
#         return 'f'

# class B(A):
#     # a = 3
#     a = A().a + 2

#     def info(self):
#         res = super().info()
#         print(res*2)
#         print('Hello2')
# a = A()
# b = B()
# # print(a.a)
# # print(b.a)
# a.info()
# b.info()



# class A:
#     def info(self):
#         return 'hello'


# class B(A):
#     def info(self):
#         return super().info() + ' world'

# obj1 = A()
# obj2 = B()
# print(obj1.info())
# print(obj2.info())


# class MyStr(str):
#     def upper(self):
#         return super().upper() + ' Нет такого метода!'

# some_str = MyStr('asdfggh')
# print(some_str.upper())




# class A:
#     pass


# class B(A):
#     pass


# class C(A):
#     pass

# a = A()
# b = B()
# c = C()

# print(isinstance(a, A))
# print(isinstance(b, A))
# print(isinstance(c, A))
# print(isinstance(a, B))
# print(issubclass(A, B))
# print(issubclass(B, A))
# print(issubclass(str, A))
# print(issubclass(C, A))






# class Person:

#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return self.name

# class Employee(Person):
#     def __init__(self, name, company):
#         super().__init__(name)
#         self.company = company

#     def __str__(self):
#         return super().__str__() + ' ' + self.company
    

# obj1 = Person('John')  
# print(obj1)
# obj2 = Employee('Nick', 'Data0X')
# print(obj2)





        

