#######Exercise 1#######
import random
def dice():
    return random.randint(1,6)
num = int(input("how many dice do you want to roll? : "))
sum = 0
for i in range(num):
    sum += dice()
print(f"The sum is: {sum}")
#######Exercise 2#######
num = []
n = input("Enter a number: ")
if(n!=''):
    while(n!=''):
        num.append(int(n))
        n = input("Enter a number: ")
    num.sort(reverse=True)
    for i in range(5):
        print(num[i])
#######Exercise 3#######
num = int(input("Enter a number: "))
prime = True
for i in range(2,num):
    if(num%i == 0):
        prime = False
if(prime==True):
    print("The number is a prime number")
else : print("The number is not a prime number")
#######Exercise 4#######
city = []
for i in range(5):
    city.append(input())
for i in city:
    print(i)