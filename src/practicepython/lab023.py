class student:
    def __init__(self,name,roll_no,total_marks):
        self.name=name
        self.roll_no=roll_no
        self.total_marks=total_marks

    def display_info(self):
        print("name=",self.name)
        print("roll_no=", self.roll_no)
        print("total_marks=", self.total_marks)
rohit10=student("Rohit",5,700)

saneep20=student("saneep",6,500)
rohit10.display_info()
saneep20.display_info()