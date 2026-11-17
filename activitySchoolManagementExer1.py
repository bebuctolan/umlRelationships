class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_id(self):
        print(f"Name: {self.name} ")
        print(f"Age: {self.age}")

person1 = Person("Panda", 21)
person1.show_id()