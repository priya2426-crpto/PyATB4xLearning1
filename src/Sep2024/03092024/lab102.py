#encapsulation

class Car:
    model=None
    name=None
    password=123

    def __init__(self):
        print("dc")
    def change_password(self):
        self.password="pramod"
    def change_password2(self):
        print(self.password)


object_ref=Car()
print(object_ref.password)
object_ref.change_password2()