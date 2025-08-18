# Private and protected
class Vehicle():
    def _display_car_info(self):
        print("Car is going at 60 km/h")

    def __display_engine_info(self):
        print("Secret engine info")

class Car(Vehicle):
    def call_protected(self):
        self._display_car_info()   # This works

    def call_private(self):
        self._Vehicle__display_engine_info() # This also works
        
    def call_private_with_error(self):
        self.__display_engine_info()    # This doesn't work, I get a AttributeError:
                            # 'Child' object has no attribute '_Child__private'

# Example usage
if __name__ == "__main__":
    my_car = Car()
    
    my_car.call_protected()
    my_car.call_private()
    my_car._display_car_info()  # This works too. Because the underscore is only a convention for protected stuff. Not a real enforcement
    my_car.call_private_with_error()