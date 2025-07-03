# Class with inheritance example
class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print("Behaviour 1")
        print(f"Vehicle Info: {self.year} {self.make} {self.model}")
        print("Behaviour 2")
        print("Behaviour 3")
        

    def start_engine(self):
        print(f"The engine of the {self.year} {self.make} {self.model} is starting.")
        # Peculiar behaviour\
        self.peculiar_behaviour()
        print("We are good to go!")
        
    def peculiar_behaviour(self):
        pass # Placeholder for peculiar behaviour, can be overridden in subclasses
        
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")
        
    def peculiar_behaviour(self):
        print("Pecualiar behaviour of Car: Honking the horn!")
        
class Truck(Vehicle):
    def __init__(self, make, model, year, payload_capacity):
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity

    def display_info(self):
        super().display_info()
        print(f"Payload capacity: {self.payload_capacity} kg")
        
    def peculiar_behaviour(self):
        print("Peculiar behaviour of Truck: Revving the engine loudly!")

# Example usage
if __name__ == "__main__":
    my_car = Car("Toyota", "Camry", 2020, 4)
    my_truck = Truck("Ford", "F-150", 2019, 1000)

    # print("Car details:")
    # my_car.display_info()
    
    # print("\nTruck details:")
    # my_truck.display_info()
    
    print("Starting car engine:")
    my_car.start_engine()
    print("\nStarting truck engine:")
    my_truck.start_engine()