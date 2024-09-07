#multiple inhertence

class father():


    def father_money(self):
        return 5

    def home(self):
        return "this is from the father"

class mother:
    def mother_money(self):
        return 2
    def home(self):
        return "this is from the mother"

class son(mother,father):#MRO method resolution order
    pass

class son2(father,mother):#MRO method resolution order
    pass
s=son()
print(s.father_money())
print(s.mother_money())
print(s.home())
s2=son2()
print(s2.home())