#inheritence--> inheritence is cquire the attributes an behaviour from another class.
#that allows a class to inherit attributes an methos parent class
# single--->85% use this in API testing,web automation,
# multiple,hybrid,multilevel
#self is efault parameter an you can access the instance variable
class father:
    key="2bHK"

    def car(self):
        print("father car!","ALTO")

class son(father):
    pass
    def home(self):
        print("3bhk")

    def truck(self):
        print("truck")

father_obj=father()
father_obj.car()
#print(father_obj.key2)

son_obj=son()
son_obj.car()
son_obj.truck()