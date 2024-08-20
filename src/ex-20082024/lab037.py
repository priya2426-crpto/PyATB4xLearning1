#grade calculator
#write a program that calculates and display the lette grade
# for a given numerial score(e.g. A,B,c,D or F)
# based on the following scale.

#A:90-100
#B:80-89
#c:70-79
#D:60-69
#F:0-59
#1--> user input--> score-->int
#2--> o/p--> str--> A or B

score=int(input("Enter the score\n"))
#grade="F"

if score>=90 and score<=100: # simply cainnig format-->90 <=score<=100
    print("your garde is","A")
elif score>=80 and score<=89: # simply cainnig format-->80 <=score<=89
    grade="B"
    print("your garde is","B")
elif score>=70 and score<=79: # simply cainnig format-->70 <=score<=79
    grade="C"
    print("your garde is","C")
elif score>=60 and score<=69: # simply cainnig format-->60 <=score<=69
    grade="D"
    print("your garde is","E")
elif score>=100:
    print("you are superman!")
else:
    print("your grade is","F")
