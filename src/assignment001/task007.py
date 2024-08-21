"""create aprogram that determines whether a given year is a leap year.
A leap year is divisible by 4,but not by 100 unles it is also divisible by 400.
use if-else statement to make this determination
"""
year=int(input("enter the year\n"))
if year %4==0 and year %100!=0:
    print(f"the {year} is a Leap year")
elif year%400==0:
    print(f"the{year} is a Leap year")
else:
    print(f"{year} is not a Leap year")
