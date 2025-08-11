from abc import ABC,abstractmethod

class Car(ABC):

    @abstractmethod
    def b(self):
        pass
class BMW(Car):

    def b(self):
        print("breaks applied")

car1 = BMW()
car1.b()