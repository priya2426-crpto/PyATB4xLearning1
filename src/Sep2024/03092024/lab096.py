a=10
class person:
    b=11

    def print_info(self):
        global a    #declare as globals
        a="hello"
        print(a)
        print(self.b)



object_ref=person()
object_ref.print_info()