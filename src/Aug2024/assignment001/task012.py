# create a program of employee class
# Att=name,age,phone,address,eid
# Beh=walk,talk,printetails
#with the constructor which will set the value
#ask the user about the information for E1 an E2
#print the etails of E1 anE2 via the print employee functions


class Employee:
    Name=None
    age=None
    phone_no=None
    address=None
    Eid=None

    def __init__(self,Name,age,phone_no,address,Eid):

        self.Name = Name
        self.age = age
        self.phone_no=phone_no
        self.address=address
        self.Eid=Eid


    def detail(self):
        print(f"employee name-->{self.Name}||employee age-->{self.age}||Employee phone No-->{self.phone_no}||employee address-->{self.address}||employee Eid-->{self.Eid}")

    def talk(self):
        print("")

    def walk(self):
        print("Employee detail")

employee_name=input("enter employee name:")
employee_age = int(input("enter employee age:"))
employee_phone_no = int(input("enter employee phone_no:"))
employee_address = input("enter employee address:")
employee_Eid= input("enter employee Eid:")

E1=Employee(employee_name,employee_age,employee_phone_no,employee_address,employee_Eid);
E1.walk()
E1.detail()

