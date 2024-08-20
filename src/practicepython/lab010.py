"""python calculator nsuch as result will be displayed based in operation"""
print("choose a operation")
print("1- Add")
print("2- sub")
print("3- mul")
print("4- div")

option=int(input("choose an operation:"))
if(option in [1,2,3,4]):

    Num1=int(input("enter the Num1"))
    Num2=int(input("enter the Num2"))

if(option==1):
    result=Num1+Num2
elif(option == 2):
    result = Num1 - Num2
elif(option == 3):
    result = Num1 * Num2
elif(option == 4):
    result = Num1 / Num2
else:
    print("invalid option")

#print("the result of the operation is{}",format(result))
