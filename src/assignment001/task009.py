"""write a program that prints number from1 to 100, however, for the multiples of 3,
print"fizz" instead of number, and for the multile of 5 print"buzz, the number multiple of 3 and 5 is fizzbuzz """
for i in  range(1,101):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    else i %3==0:
        print("fizz")
    else i %5==0:
        print("buzz")
    else:
        print(i)
