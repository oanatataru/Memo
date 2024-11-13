class Vehicle:
    """Base class for vehicles"""

    def __init__(self, make, model, year, mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, distance):
        """Increase mileage based on distance driven"""
        if distance > 0:
            self.mileage += distance
            print(f"Drove {distance} miles. Total mileage: {self.mileage} miles.")
        else:
            print("Distance must be positive.")

    def get_info(self):
        """Display basic vehicle information"""
        return f"{self.year} {self.make} {self.model}, Mileage: {self.mileage} miles"


class Car(Vehicle):
    def __init__(self, make, model, year, mileage=0, fuel_efficiency=25):
        super().__init__(make, model, year, mileage)
        self.fuel_efficiency = fuel_efficiency  # Miles per gallon

    def calculate_mileage(self, gallons):
        """Calculate distance that can be driven with a given fuel amount"""
        if gallons > 0:
            distance = gallons * self.fuel_efficiency
            print(f"With {gallons} gallons, this car can drive {distance} miles.")
            return distance
        else:
            print("Gallons must be positive.")
            return 0


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mileage=0, fuel_efficiency=50):
        super().__init__(make, model, year, mileage)
        self.fuel_efficiency = fuel_efficiency  # Miles per gallon, usually higher for motorcycles

    def calculate_mileage(self, gallons):
        """Calculate distance that can be driven with a given fuel amount"""
        if gallons > 0:
            distance = gallons * self.fuel_efficiency
            print(f"With {gallons} gallons, this motorcycle can drive {distance} miles.")
            return distance
        else:
            print("Gallons must be positive.")
            return 0


class Truck(Vehicle):
    def __init__(self, make, model, year, mileage=0, towing_capacity=10000):
        super().__init__(make, model, year, mileage)
        self.towing_capacity = towing_capacity  # Maximum weight in pounds

    def calculate_towing_capacity(self, weight):
        """Check if the truck can tow a given weight"""
        if weight <= self.towing_capacity:
            print(f"This truck can tow {weight} pounds.")
            return True
        else:
            print(f"This truck cannot tow {weight} pounds. Max capacity: {self.towing_capacity} pounds.")
            return False


# Example usage
car = Car(make="Toyota", model="Camry", year=2020, mileage=5000, fuel_efficiency=30)
motorcycle = Motorcycle(make="Harley-Davidson", model="Sportster", year=2019, mileage=3000, fuel_efficiency=55)
truck = Truck(make="Ford", model="F-150", year=2021, mileage=15000, towing_capacity=13000)

# Display information and specific functionality
print(car.get_info())
car.calculate_mileage(10)  # Calculate mileage based on fuel amount

print(motorcycle.get_info())
motorcycle.calculate_mileage(5)  # Calculate mileage for motorcycle

print(truck.get_info())
truck.calculate_towing_capacity(12000)  # Check towing capacity
truck.calculate_towing_capacity(14000)  # Exceeds towing capacity
