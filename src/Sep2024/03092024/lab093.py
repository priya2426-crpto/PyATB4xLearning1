class person:


    def __init__(self):
        self.name = input("enterthe name\n")
        self.age = input("enterthe age\n")
        self.phone = input("enterthe phone\n")
        self.occupation = input("enterthe occupation\n")


    def name_of_the_function(self):
        print(f"name is{self.name}")
        print(f"age is{self.age}")
        print(f"phone is{self.phone}")
        print(f"0ccupation is{self.occupation}")

p1=person()
