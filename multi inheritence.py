
class Parent:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet(self):
        print("Hello")

class Child(Parent):

    def sound(self):
        print(f"I'm {self.name}")


#hierarchical

class Child2(Parent):

    def sound(self):
        print("hierarchical inheritence")
    
    def car(self):
        print("I'm having lambo")


#Multiple, multi-level

class Grandchild(Child,Child2):

    def sound(self):
        print(f"I'm {self.name}, implementing multi level inheritence")

c1 = Grandchild("rahul",1)
c1.sound()
