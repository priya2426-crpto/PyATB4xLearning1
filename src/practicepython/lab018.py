

old_password="abcd"
for i in range(1,6):
    password=input("enter password")

    if old_password==password:
        print("Login successfuly")
        break

print("You have ",5-i,"attempt left")