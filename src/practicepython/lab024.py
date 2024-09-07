class bank:
    def __init__(self,account_no,balance):
        self.account_no=account_no
        self.balance=balance

    def deposite(self):
        Amount=float(input("enter the amount to deposite"))
        self.balance=self.balance+Amount
        print("money deposite successfully")
    def withdrawl(self):
        Amount=float(input("enter the amount to withdrawl"))
        if Amount>self.balance:
            print("low balance")
        else:
            self.balance=self.balance-Amount
            print("money withdrawl successfully")

    def display_balance(self):
        print("your balance=",self.balance)
rohit10=bank(12345,5000)
rohit10.deposite()
rohit10.withdrawl()
rohit10.display_balance()
