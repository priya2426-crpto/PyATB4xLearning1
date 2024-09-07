class person:
    #name="amit" #common across all the variable so cant use like this

    def __init__(self,name):  # constructor is used change the instance value of variable
        self.name=name
    def walk(self,name):
        print(self.name)

amit=person("amit")
parmod=person("parmod")
print(amit.name)
print(parmod.name)
print("who is walking with the object of pramod",parmod.walk())
