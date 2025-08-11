class Parent:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello")

class Child(Parent):

    def sound(self):
        print(f"I'm {self.name}")

c1 = Child("lekha",1)
c1.sound()