"""1.no return type an no parameter"""
def greet():
    print("hello world!")


result=greet()
print(result)
"""2.no return type wit argument"""
def greet_by_name(name):
    print("hello",name.upper())

greet_by_name("pramod")
#greet_by_name( )
greet_by_name(name="tushar")

def multiple_args(name1="Arpita",name2="Pramod",name3="amit"):
    print("Multiple arguments",name1,name2,name3)
multiple_args(name1="Ram",name2="Yunus",name3="nisha")
multiple_args()

"""4. argument+ return type"""

def Sum_of_two_number(Num1,Num2):
    return Num1+Num2
result=Sum_of_two_number(10,5)
print(result)

""" no return type an with default argument"""

def say_hello_default_arg(name="pramod"):
    print("hello",name)

say_hello_default_arg("amit")
say_hello_default_arg