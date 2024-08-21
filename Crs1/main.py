########### Exercise 1 ###########

name = "Zongru Li"
print("Hello,",name)

########### Exercise 2 ###########

#1
name = input("Please input your name: ")
print("Hello,",name,"!")

#2
radius = int(input("Please enter the radius: "))
area = radius **2 *3.14
print("The area is",area)

#3
length = int(input("Please enter the length: "))
width = int(input("Please enter the width: "))
area = length * width
perimeter = 2 * (length + width)
print("The perimeter is:",perimeter,"\nThe area is:",area)

#4
num1=int(input("Please enter the first number: "))
num2=int(input("Please enter the second number: "))
num3=int(input("Please enter the third number: "))
print("The sum is:",num1+num2+num3)
print("The product is:",num1*num2*num3)
print("The average is:",(num1+num2+num3)/3)

#5
from decimal import *
talents = float(input("enter talents: "))
pounds = float(input("enter pounds: "))
lots = float(input("enter lots: "))

pounds += talents * 20
lots += pounds * 32
grams = lots * 13.3
kilograms = int(grams/1000)
grams = grams - kilograms*1000
print(kilograms,"kilograms and",round(grams,3),"grams")