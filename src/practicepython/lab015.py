old_password="abcd"
password=input("enter password")

while old_password!=password:
    print("invalid password")
    password=input("enter password")
print("welcome")