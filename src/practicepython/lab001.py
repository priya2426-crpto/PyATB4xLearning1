# left half pyramid pattern
n=6
for i in range(n+1):
    for j in range(2*n-1):
        print("",end="")
    for j in range(i):
        print("*",end="")
    print()