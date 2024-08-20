#problem find the max between 3 numbers

#logic building
#user imput--> num1,num2,num3-->int
#o/p-->int or string with max number
# logic ? if alse- 1 condition
# more 1 condition --> if elif else
# syntax
"""if condition 1:
    print("do 1")
elif condion 2:
    print("do 2")
if condition 3:
     print("do 3")"""

num1=int(input("enter the num1\n"))
num2=int(input("enter the num2\n"))
num3=int(input("enter the num3\n"))
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)


# by using Max function
#result=max(num1,num2,num3)
#print(result)