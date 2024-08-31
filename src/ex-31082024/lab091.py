#constructor
#special function in clss,__init__()
class Dog:
    name=None
    age=None

    def __init__(self,name,age):
        print("called,object is created")
        self.name=name
        self.age = age

    def sleep(self):
        print("sleeping")
        print(" who is sleeping-->",self.name,self.age)
        return None

dog1=Dog("chow",10)
print(dog1.name)
dog1.sleep()

dog2=Dog("mow",20)
print(dog2.name)
dog2.sleep()