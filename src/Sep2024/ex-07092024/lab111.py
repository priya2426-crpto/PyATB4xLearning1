#abstaction--> hide the etails an show what is required (hiding my own classes)(actually means
#car-->ket__private,tyre-->public
#car-->multiple-engine,gearbox
from abc import ABC, abstractclassmethod
class father(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def loan(self):
        pass

class pramo(father):
    pass
    def loan(self):
        print("pai the loan")

obj=pramo()
obj.loan()