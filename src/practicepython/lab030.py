class car:

    def __init__(self,brand):
        self.brand=brand

    def car_detail(self):
        print("this is a car")
class electric_car(car):
    def __init__(self,No_of_batteries,brand,seating_capacity):
        car.__init__(self,brand)
        self.No_of_batteries=No_of_batteries

    def elect_car_details(self):
        print("this is a electric car")
class electric_suv(electric_car):
    def __init__(self,brand,No_of_batteries,model):
        electric_car.__init__(self,No_of_batteries,brand)
        self.model=model

e_car=electric_car("moel x","tesla",50)
print(e_car.model)
print(e_car.No_of_batteries)
print(e_car.brand)