class Dog:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age


class DogBuilder:
    def __init__(self):
        self.dog = Dog()

    def set_name(self, name):
        self.dog.name = name
        return self

    def set_age(self, age):
        self.dog.age = age
        return self

    def build(self):
        return self.dog


# dog_build = DogBuilder()
# dog_build.set_name("Doguinho")
# dog = dog_build.build()

dog = DogBuilder().set_name("Doguinho").build()


print(dog.name)