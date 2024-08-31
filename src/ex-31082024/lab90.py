class Dog:
    Name=None
    bread=None
    color=None

    def sleep(self):
        print("sleeping")

    def bark(self):
        print("bark")

    def eat(self):
        print("food")

dog1= Dog()
#print(dog1.Name)
dog1.Name="chow"
print(dog1.Name)
dog1.sleep()
print("______________")

dog2=Dog()
#print(dog2.Name)
dog2.Name="mow"
print(dog2.Name)
dog2.bark()




