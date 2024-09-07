class car:
    def __init__(self,o_name,o_make,o_moel):
        self.name=o_name
        self.make=o_make
        self.moel=o_moel
    def start_engine(self):
        print("starting a car with the name"+self.name)
        print("starting a car with the make" + self.make)
        print("starting a car with the mole" + self.mole)

lambo=car("lambo","v2","2024")
lambo.start_engine()