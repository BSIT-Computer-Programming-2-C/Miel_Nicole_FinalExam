class Person:
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age
        self.__address = address

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:  
            self.__age = age
        else:
            print("Age must be non-negative")

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address


person = Person("Miel Nicole C. PAy-oen", 20, "Upper Camp")

print(f"Name: {person.get_name()}")
print(f"Age: {person.get_age()}")
print(f"Address: {person.get_address()}")

person.set_name("Riza Mae Valenzuela")
person.set_age(20)
person.set_address("La Trinidad Km4 Mamaga")

print("\nUpdated Information:")
print(f"Name: {person.get_name()}")
print(f"Age: {person.get_age()}")
print(f"Address: {person.get_address()}")
