#factorial of number
num=int(input("enter the number "))
if num<0:
    print("wrong input")
elif num==0:
    print("factorial ",1)
else:
    fact = 1
    for i in range(1,num+1):
        fact=fact*i

        print("factorial of",num,"is", fact)


