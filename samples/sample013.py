class Number():
    def __init__(self, value):
        # Initialize the Number class with a value
        # and assign it to the instance variable
        # self.value
        # The __init__ method is a constructor in Python
        # that is called when an object of the class is created
        # It is used to initialize the attributes of the class
        # The self parameter refers to the instance of the class
        # and allows us to access its attributes and methods
        # The value parameter is passed when creating an instance
        # of the class and is assigned to the instance variable
        self.value = value

    def display(self):
        print(f"Number: {self.value}")

num = Number(10)
num.display()


class Person():
    population = 50  # Class variable to keep track of the population
    def __init__(self, name, age):
        # Initialize the Person class with a name
        # and assign it to the instance variable
        # self.name
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(self):
        # Return the population of the class
        return Person.population
    
    @staticmethod
    def isAdult(self):
        # Return the population of the class
        return self.age >= 18
    

person = Person("John", 25)

print(person.getPopulation())  # Output: 50