"""create program,take 2 inputs from the user num1 & num2
 and give them max,pow,mul,div,sum,sub
 Format your output to f{""}"""
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
print(num1)
print(num2)
print("Max of",num1,"and",num2, "is:",max(num1,num2))
print("value of",num1,"to the power of",num2, "is:",pow(num1,num2))
print("Mul of",num1,"and",num2, "is:",num1*num2)
print("Sum of",num1,"and",num2, "is:",num1+num2)
print("Sub of",num1,"and",num2, "is:",num1-num2)
print("Div of",num1,"and",num2 ,"is:",num1/num2)

print("formated_num1 is:"f"{num1:.5f}")
print("formated_num2 is:"f"{num2:.5f}")