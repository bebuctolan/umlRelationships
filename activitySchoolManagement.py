class Person():
    def __init__(self, name, __age):
        self.name = name
        self.__age = __age
    def show_id(self):
        print(f"Name: {self.name} ")
        print(f"Age: {self.get_age()}")
    def get_age(self):
        return self.__age

person1 = Person("Panda", 21)
person1.show_id()


        
