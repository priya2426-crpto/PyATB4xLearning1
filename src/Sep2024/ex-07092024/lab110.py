#method overloading is not support in python
class MathUtils(object):
    def add(self,a,b):
        return a+b

    def add(self, a, b,c=0):
        return a + b+c #
    def add(self, a, b,c=0,d=1):
        return a + b+c+d #

Math=MathUtils()
op1=Math.add(1,2)
print(op1)