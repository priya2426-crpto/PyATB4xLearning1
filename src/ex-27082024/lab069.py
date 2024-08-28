def a_before_ui_after_ui(func):
    def wrapper():
        print("Before the running UI ")
        print("start the browser")
        func()
        print("ening the running UI")
        print("quit the browser")
    return wrapper()
@a_before_ui_after_ui
def test_ui():
    print("I will test the ui ")
#test_ui()