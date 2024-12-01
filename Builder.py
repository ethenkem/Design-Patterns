"""
The idea is if we want to make a burger we dont put all
the needed parameters in at ones but add them one at a time 
"""


class Car:
    def __init__(
        self,
    ) -> None:
        self.color = None
        self.brand = None
        self.top_speed = None

    def set_color(self, color):
        self.color = color

    def set_brand(self, brand_name):
        self.brand = brand_name

    def set_top_speed(self, top_speed):
        self.top_speed = top_speed

    # just for logging
    def __str__(self) -> str:
        return f"""{
            {"brand": self.brand,
            "color": self.color,
            "top_speed": self.top_speed
            }
             }"""


# Our Builder
class CarBuilder:
    def __init__(self) -> None:
        self.car = Car()

    def add_color(self, color):
        self.car.set_color(color)
        return self

    def add_brand(self, brand):
        self.car.set_brand(brand)
        return self

    def add_top_speed(self, top_speed):
        self.car.set_top_speed(top_speed)
        return self

    # after adding all the staffs that we want we finally build the car
    def build(self):
        return self.car


car = (
    CarBuilder()
    .add_brand("toyota")
    .add_brand("lexus")
    .add_color("red")
    .add_top_speed("3453km/hr")
    .build()
)

print(str(car))
