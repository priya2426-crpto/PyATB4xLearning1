#logic building formula
# step 1 figure outthe input and output
#input--> r--> datatype-->float
#Pi=3.14
#power=pow or **--> any

#o/p--> float-area,print area

#Step2
#rough logic=area=3.14*pow(r,2)

#step3- write the logic
import math
radius=float(input("enter the radius of the circle\n"))
print(radius)
print(math.pi)
area=math.pi*math.pow(radius,2)
area2=3.14*(radius**2)
print("area of circle is-->",area)
print("area of circle is-->,{area:.2f}")
print("area of circle is-->,{area2:.2f}")
