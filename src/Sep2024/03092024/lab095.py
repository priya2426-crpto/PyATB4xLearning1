class calc:
    def __init__(self):

        print("dc")

    def sum(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        return a/b

object_created = calc()
a=int(input("enter the value of a"))
b=int(input("enter the value of b"))

output_sum=object_created.sum(a,b)
output_sub=object_created.sub(a,b)
output_mul=object_created.mul(a,b)
output_div=object_created.div(a,b)
print(output_sum,output_sub,output_mul,output_div)