from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def move(self):
        pass


# Se quiser ter mais abstratos, esse não precisaria implementar nada ainda
class Dog(Animal, ABC):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print("MOVIDO")

d1 = Dog("Doguinho")
d1.move()