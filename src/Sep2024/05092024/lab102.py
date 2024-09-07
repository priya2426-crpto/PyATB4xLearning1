class bank:
    def __init(self,account_number,balance):
        self.balance="balance"
        self.account_number=account_number
    def deposite(self,amount):
        self.balance=self.balance+amount
    def check_balance(self):
        print(self.balance)


    def show_me_account_number(self,is_auth):
        if is_auth=="True":
            print(self.account_number)
        else:
            print("not allowed")

icici=bank(64412,100)
icici.deposite(100)
icici.check_balance()
icici.show_me_account_number(False)
icici.deposite(100)
icici.check_balance()


