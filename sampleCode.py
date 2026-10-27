from typing import List, Optional

class Animal:
    def eat(self) -> None:
        print("This animal is eating.")

class Dog(Animal):
    
    def bark(self) -> None:
        print("The dog is barking: Woof! Woof!")


from abc import ABC, abstractmethod

class Payable(ABC):
    @abstractmethod
    def pay(self) -> None:
        pass

class Payment(Payable):
    def pay(self) -> None:
        print("Processing payment via Payment class implementation.")


class Room:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

class House:
    def __init__(self):
    
        self.rooms: List[Room] = [
            Room("Living Room"),
            Room("Bedroom")
        ]

    def show_rooms(self) -> None:
        print("House has the following rooms:")
        for room in self.rooms:
            print(f"- {room.get_name()}")

class Book:
    def __init__(self, title: str):
        self.title = title

    def get_title(self) -> str:
        return self.title

class Library:
    def __init__(self, books: List[Book]):

        self.books = books

    def show_books(self) -> None:
        print("Library contains these books:")
        for book in self.books:
            print(f"- {book.get_title()}")



class Order:
    def __init__(self, order_id: int):
        self.order_id = order_id
    
    def get_order_id(self) -> int:
        return self.order_id

class Customer:
    def __init__(self, name: str, orders: List[Order]):
        self.name = name
        self.orders = orders  

    def show_customer_orders(self) -> None:
        print(f"Customer {self.name} has placed these orders:")
        for order in self.orders:
            print(f"Order ID: {order.get_order_id()}")


class Document:
    def __init__(self, content: str):
        self.content = content

    def get_content(self) -> str:
        return self.content

class Printer:
    def print_doc(self, doc: Document) -> None:  
        print(f"Printing document content: {doc.get_content()}")

if __name__ == "__main__":
    print("=== 1. INHERITANCE ===")
    my_dog = Dog()
    my_dog.eat()
    my_dog.bark()

    print("\n=== 2. REALIZATION ===")
    payment = Payment()
    payment.pay()

    print("\n=== 3. COMPOSITION ===")
    my_house = House()
    my_house.show_rooms()

    print("\n=== 4. AGGREGATION ===")
    book_list = [Book("Python Programming"), Book("Algorithms")]
    my_library = Library(book_list)
    my_library.show_books()

    print("\n=== 5. ASSOCIATION ===")
    order_list = [Order(201)]
    customer = Custom = Customer("Bob", order_list)
    customer.show_customer_orders()

    print("\n=== 6. DEPENDENCY ===")
    my_doc = Document("UML Python Notes")
    printer = Printer()
    printer.print_doc(my_doc)  
