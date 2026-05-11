
black_lady = {
    "name": "Black Lady",
    "age": 17,
    "city": "Tokyo",
    "occupation": "Student",
    "hobbies": ["Reading", "Traveling", "Gaming"],
    "is_student": True,
    "status": "Single"
}
print(black_lady)
print(black_lady["status"])


class Person:
    def __init__(self, name, age, city, occupation, hobbies, is_student, status):
        self.name = name
        self.age = age
        self.city = city
        self.occupation = occupation
        self.hobbies = hobbies
        self.is_student = is_student
        self.status = status

black_lady = Person("Josefína", 17, "Tokyo", "Student", ["Gaming"], True, "Single")
print(black_lady.status)

class Car:
    def __init__(self, brand, model, year, color, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def drive(self, driver):
        return driver + " is driving a " + self.color + " " + self.brand + " " + self.model

    def crash(self, driver):
        return self.model + " crashed by " + driver

bmw = Car("BMW", "X5", 2020, "Black", 15000)
print(bmw.drive("Woman"))
print(bmw.crash("Woman"))

class Book:
    def __init__(self, name, author, num_of_pages):
        self.name = name
        self.author = author
        self.num_of_pages = num_of_pages

    def about(self):
        return self.name + " is written by " + self.author + " and has " + str(self.num_of_pages) + " pages."
    def read(self, reader):
        return reader + " is reading " + self.name
    
about = Book("Fronta", "George Orwell", 328)
print(about.about())

read = Book("Fronta", "George Orwell", 328)
print(read.read("Petr")) 