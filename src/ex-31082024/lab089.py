#PyATB Stuents
# attibutes - name,i,phone no,gener,color eye,city,location

class Person:
    #attributes
    i=None
    name=None
    age=None
    email=None
    height=None
    gener=None
    phone_no=None
    pta=None

    #behaviour
    def talk(self,name):    # arg with no return type
        print("i can talk")
    def sleep(self,name):    # arg with no return type
        print("i am a metho")
        print("sleep",name)

    def talk(self,name):    # arg with no return type
        print("i am a metho")
        print("sleep",name)

    def walk_return(self):
        return "I am walking"

tushar=Person()
tushar.name="tushar"
print(tushar.name)
#tushar.talk

usha=Person()
usha.name="usha"
print(usha.name)
#usha.talk()



