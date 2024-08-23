#######Exercise 1#######

length = float(input("the length of a zander in centimeters: "))
limit = 42
if(length < limit):
    minus = limit - length
    print(f"The fish has been released back into the lake, {minus} centimeters below the size")
else: print("The zander fulfills the size limit")

#######Exercise 2#######

cabin_class = input("Enter the cabin class of the cruise ship: ")
if(cabin_class == 'LUX'):
    print('upper-deck cabin with a balcony.')
elif (cabin_class == 'A'):
    print('above the car deck, equipped with a window.')
elif (cabin_class == 'B'):
    print('windowless cabin above the car deck.')
elif (cabin_class == 'C'):
    print('windowless cabin below the car deck.')
else:
    print('Invalid cabin class.')

#######Exercise 3#######

gender = input('input your gender: ')
hem = int(input('input your hemoglobin value: '))
if(gender == 'female'):
    low = 117
    high = 155
else:
    low = 134
    high = 167
if(hem<low):
    print('the hemoglobin is low')
elif (hem>high):
    print('the hemoglobin is high')
else: print('the hemoglobin is normal')

#######Exercise 4#######

year = int(input('Input the year:'))
if(year%4==0):
    if(year%100!=0):
        print(f'{year} is a leap year')
    elif(year%400==0):
        print(f'{year} is a leap year')
    else: print('{year} is NOT a leap year')
else: print(f'{year} is NOT a leap year')