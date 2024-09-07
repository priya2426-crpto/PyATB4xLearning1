def my_decorator(func):
    def wrapper():
        print("something is happening before the function is called")
        print("add helmet,dashcash,gloves")
        func()
        print("something is happening after the function is called")
        print("secure driving")
    return wrapper()
@my_decorator
def drive_bike():
    print("I am driving ")
#drive_bike()

def drive_scooty():
    print("normal function ")
    drive_scooty()