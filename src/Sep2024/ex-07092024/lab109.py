#method overriding--> same name i the parent an child
#chil always riding the parent class

class father:
    a=10
    def home(self):
        print("1BHK")

class Son(father):
    b=20
    def home(self):
        super().home()
        print (super().a)
        print("no house")
        print(self.b)

priya=Son()
print(priya.home)