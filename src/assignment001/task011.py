#fibonaci series
num=int(input("enter the number to fin fibonaci series\n"))
a=0
b=1
fib=0
if num==0:
    print(0)
elif num==1:
    print(0)
else:
    for i in range(2,num+1):
        fib=a+b
        a=b
        b=fib
        print(fib)