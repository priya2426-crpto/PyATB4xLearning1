# write a program that classifies a triangle based on its side length.given three input values represnting the lengths of the sides,
# determines if the triangle is equilateral(all sides equal),isoceless(exactly two sides equal) or scalene(no sides equal)
#se an if-else statement to classify the triangle
a=int(input("enter the first length of triangle"))
b=int(input("enter the second length of triangle"))
c=int(input("enter the third length of triangle"))
if a==b==c:
    print(f"equilateral triangle")
elif a==b or b==c or a==c:
    print(f"isoceless triangle")
else:
    print("scalene triangle")