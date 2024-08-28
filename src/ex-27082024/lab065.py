public_toilet="PB"  #local variable have more
def home():
    private_toilet="PT"
    print(public_toilet)
    print(private_toilet)
    public_toilet = "LPB"
    print(public_toilet)
    home()
def strange():

    print(public_toilet)
    #print(private_toilet)

print(public_toilet)
# print(private_toilet)

strange()


