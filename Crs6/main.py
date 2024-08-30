#######Exercise 1#######
import random
def dice():
    return random.randint(1,6)
dices=0
while(dices!=6):
    dices=dice()
    print(dices)
#######Exercise 2#######
def dice(side):
    return random.randint(1,side)
side=int(input("maximum number: "))
dices=0
while(dices!=side):
    dices=dice(side)
    print(dices)
#######Exercise 3#######
def convert(value):
    value *=3.785
    return(value)
gallon = int(input("the quantity of gasoline in American gallons: "))
while (gallon >= 0):
    print(f"Value in litres is: {convert(gallon)}")
    gallon = int(input("the quantity of gasoline in American gallons: "))
#######Exercise 4#######
def sum(num):
    value = int()
    for i in num:
        value+=i
    return(value)

num = [1,5,4,3,6,666,3,114514]
print(sum(num))
#######Exercise 5#######
def check(num):
    new_num=[]
    for i in num:
        if(i%2==0):
            new_num.append(i)
    return(new_num)
num = [1,5,4,3,6,666,3,114514]
print(num)
print(check(num))
#######Exercise 6#######
def calc(diameter,price):
    diameter/=100
    radius=diameter/2
    area = radius*radius*3.14
    value = price/area
    return round(value,3)
value=[0,0]
for i in range(2):
    diameter=int(input(f'Enter the diameter of pizza{i+1}: '))
    price=int(input(f'Enter the price of pizza{i+1}: '))
    value[i]=calc(diameter,price)
if(value[0]<value[1]):
    print(f'The first one provides better value for money,{value[0]}>{value[1]}')
else:
    print(f'The second one provides better value for money,{value[0]}<{value[1]}')