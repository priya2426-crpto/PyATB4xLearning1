#condition and loops

#write aa program to take a user age and let him know i he can go the club.

#1. user inpur==? dta type-->
#o/p-->string

#2.rough logic
# age=>21-->print can go
#age<21--> can't go
# write the logic


age=int(input("enter your age\n"))
if age>21:
    print(f"can go to club--->{age}")
else:
    print(f"can't go  to club---{age}")