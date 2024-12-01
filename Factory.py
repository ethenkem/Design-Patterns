"""
in the factory pattern instead of instantiating a new oject directly
you do that with a method or a class. let a factory class do it for you with
with you just specifing what you want
"""


class Vehicle:
    def __init__(self, vehicle_detail: list[str]) -> None:
        self.vehicle_details = vehicle_detail

    def print_vehicle(self):
        print(self.vehicle_details)


class CarFactory:
    def createCar(self):
        vehicle_details = ["Toyata", "yelloe & black", "6734.54"]
        return Vehicle(vehicle_details)

    def createBus(self):
        vehicle_details = ["Daewoo", "white", "35535.33"]
        return Vehicle(vehicle_details)

    def createMotoBike(self):
        vehicle_details = ["Royal", "white", "445.64"]
        return Vehicle(vehicle_details)


# now all we have to do is tell the factory what kind of vehicle
car_factory = CarFactory()
# create bus vehicle
car_factory.createBus().print_vehicle()

# create car vehicle
car_factory.createCar().print_vehicle()

# create a motor bike
car_factory.createMotoBike().print_vehicle()
