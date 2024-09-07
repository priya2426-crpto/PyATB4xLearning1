class VWOLoginPage:

    def __init__(self,email_arg,password_arg):
        self.email=email_arg
        self.password = password_arg
    def login_confirm(self):
         if self.email=="pramo@gmail.com" and self.password=="12345":
            print("login sucessfully")
         else:
             print("invali login")
email=input("enter the email\n")
password=input("enter the password\n")
VWO_obj=VWOLoginPage(email,password)
VWO_obj.login_confirm()