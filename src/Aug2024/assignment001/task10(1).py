num=int(input("enter the number "))
fact = 1
while num>=0:
    for i in range(1,num+1,1):
        fact=fact*i

        print("factorial of",num,"is", fact)
