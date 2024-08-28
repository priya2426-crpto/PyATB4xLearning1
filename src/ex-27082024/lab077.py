def find_odd_even(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
find_odd_even(5)

check_find_odd_even=lambda num:"even" if num%2==0 else "odd"
print(check_find_odd_even(5))

