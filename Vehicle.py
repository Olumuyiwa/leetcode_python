class Vehicle:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type
        self.gas_tank_size = 14
        self.fuel_level = 0

    def fuel_up(self):
        self.fuel_level = self.gas_tank_size
        print("The gas tank is now full.")

    def drive(self):
        print(f'The {self.model} is now driving')

vehicle_object = Vehicle("Toyota", "Corolla","Sport")
print("The vehicle object is ",vehicle_object)
print("The vehicle is a ",vehicle_object.model,vehicle_object.brand,vehicle_object.type)
vehicle_object.fuel_up();
vehicle_object.drive();
