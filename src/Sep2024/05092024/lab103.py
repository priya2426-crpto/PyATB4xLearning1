class MYclass:
    public_var="i am public"
    balance=100

    __private_var="i am private"
    __password="1234"
    _protected_var="i am protected"
    b=20
    _c=30
    __e=50

object=MYclass()
print(object.public_var)
print(object._protected_var)
#print(object.__e=50)