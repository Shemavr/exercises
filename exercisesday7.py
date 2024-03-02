class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"name = {self.name}, age ={self.age}"
    
person1 = Person("Elisa", 39)
print(person1)
# print("Name:", person1.name)
# print("Age:", person1.age)

# class Animal:
#     def sing(self):
#         pass  # Placeholder method to be overridden by subclasses

# class Dog(Animal):
#     def sing(self):
#         print("Woof!")

# class Cat(Animal):
#     def sing(self):
#         print("Meow!")

# class Bird(Animal):
#     def sing(self):
#         print("Chirp!")

# # Creating instances of different animals
# dog = Dog()
# cat = Cat()
# bird = Bird()

# # Calling sing() method for each animal
# dog.sing()  
# cat.sing()  
# bird.sing()  

# class Employee:
#     def __init__(self, name, position, salary):
#         self.name = name
#         self.position = position
#         self.salary = salary

#     def __str__(self):
#        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}"
    
# class Manager(Employee):
#     def __init__(self, name, position, salary, department):
#         super().__init__(name, position, salary)
#         self.department = department

#     def __str__(self):
#         return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Department: {self.department}"
    
# a = Manager ("Ayo", "Manager", 5000, "Admin")
# print(a)
# b= Employee("Ayo", "IT", 3000)
# print(b)