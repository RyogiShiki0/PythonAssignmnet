########### Exercise 1 ###########
season = ("spring","summer","autumn","winter")
month = int(input("Please input the month: "))
if (month in (3,4,5)):
    print(season[0])
elif (month in (6,7,8)):
    print(season[1])
elif (month in (9,10,11)):
    print(season[2])
else:
    print(season[3])
########### Exercise 2 ###########
names = set()
name=input("Please input the name: ")
while(name != ''):
    if name in names:
        print('Existing name')
    else:
        print('New name')
        names.add(name)
    name = input("Please input the name: ")
print(names)
########### Exercise 3 ###########
airport = {}
select = int(input("Enter the number at the front to select: \n[1]enter a new airport\n[2]fetch the information of an existing airport\n[3]quit\n"))
while (select !=3):
    if(select == 1):
        icao = input("Please input the icao: ")
        name = input("Please input the name: ")
        airport.update({icao:name})
    else:
        icao = input("Please input the icao: ")
        if (icao in airport.keys()):
            print(airport[icao])
        else: print("The airport does not exist")
    select = int(input(
        "Enter the number at the front to select: \n[1]enter a new airport\n[2]fetch the information of an existing airport\n[3]quit\n"))