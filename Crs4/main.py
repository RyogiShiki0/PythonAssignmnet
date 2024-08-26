#######Exercise 1#######
from ctypes import pythonapi

i=1
while i in range(1000):
    if(i%3==0):
        print(i)
    i+=1
#######Exercise 2#######
inch = int(input("Enter the number of inches: "))
while(inch>0):
    inch *= 2.54
    print(inch)
    inch = int(input("Enter the number of inches: "))
#######Exercise 3#######
num=input("Enter the number: ")
if(num!=""):
    min=int(num)
    max=int(num)
    while(num!=""):
        num=int(num)
        if(num<min):
            min=num
        elif(num>max):
            max=num
        num = input("Enter the number: ")
    print(f"min={min};max={max}")
#######Exercise 4#######
import random
num=random.randint(1,10)
guess=int(input("Guess the number: "))
while(guess!=num):
    if(guess<num):
        print("too low")
    if(guess>num):
        print("too high")
    guess=int(input("Guess the number: "))
print(f"correct")
#######Exercise 5#######
num=0
while(num<5):
    usr = input("username: ")
    psw = input("password: ")
    if(usr =='python' and psw =='rules'):
        print("Welcome")
        break
    num += 1
if(num==5):
    print("Access denied")
#######Exercise 6#######
