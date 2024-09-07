#create a program that takes two numbers as input and print wheather the first number is greater
# than,less than or equal to second number.

num1=int(input("enter the First number"))
num2=int(input("enter the second number"))
if num1>num2:
    print(num1,"is grater than ",num2)
elif num1<num2:
    print(num2, "is grater than ",num1)
elif num1==num2:
    print(num1,"is equal to ",num2)
else:
    print("invalid number")


