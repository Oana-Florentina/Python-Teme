# Create a base class Vehicle with attributes like make,
# model, and year, and then create subclasses for specific
# types of vehicles like Car, Motorcycle, and Truck.
# Add methods to calculate mileage or towing capacity based on the vehicle type.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Year: {self.year}, make: {self.make}, model: {self.model};")

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency

    def calculate_mileage(self, distance):
        return distance / self.fuel_efficiency

class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def get_towing_capacity(self):
        return self.towing_capacity


car = Car(make="Toyota", model="Camry", year=2022, fuel_efficiency=25)
car.display_info()
print(f"Mileage for a 100-mile trip: {car.calculate_mileage(100)} miles")

motorcycle = Motorcycle(make="Harley-Davidson", model="Sportster", year=2022)
motorcycle.display_info()

truck = Truck(make="Ford", model="F-150", year=2022, towing_capacity=10000)
truck.display_info()
print(f"Towing capacity: {truck.get_towing_capacity()} pounds")
