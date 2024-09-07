#multilevel inheritence

class granfather():
   gold="2kg"

    def bhk1(self):
        print("1bhk")

class father(granfather):
    diamond="2 kart"

class son(father):
    print("3bhk")

s=son()
f=father()
gf=granfather()