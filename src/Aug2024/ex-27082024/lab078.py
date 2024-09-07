import math
def give_me_pow(num):
    return math.pow(num,2)
op=give_me_pow(10)
print(op)

o=lambda n:math.pow(n,2)
print(o(5))

op2=lambda :math.pow(int(input("enter the num")),2)
print(op2())