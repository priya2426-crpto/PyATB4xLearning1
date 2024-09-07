#BMI calculator weight(kg) and height(cm)

#underweight=<18.5
#normal weight=18.5-24.9
#over weight=25-29.9
#obesity=>30

weight=float(input("enetr weight in KG"))
height=float(input("enetr height in meter"))

"""if weight<=18.5:
    print("underweight")
    elif weight=18.5 and weight<=24.5:
        print("normal weight")
    elif weight = 25 and weight <= 29.5:
        print("normal weight")
else:"""


bmi=weight/height**2
print("your BMI",bmi)