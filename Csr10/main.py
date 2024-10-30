########### Exercise 1 ###########
class elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.floor = bottom

    def go_to_floor(self, floor):
        if floor > self.floor:
            while floor > self.floor:
                self.floor_up()
        elif floor < self.floor:
            while floor < self.floor:
                self.floor_down()

    def floor_up(self):
        self.floor +=1
        print(f"Now it's on {self.floor}")

    def floor_down(self):
        self.floor -=1
        print(f"Now it's on {self.floor}")

elev = elevator(1, 20)
elev.go_to_floor(5)
########### Exercise 2 ###########
class elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.floor = bottom

    def go_to_floor(self, floor):
        if floor > self.floor:
            while floor > self.floor:
                self.floor_up()
        elif floor < self.floor:
            while floor < self.floor:
                self.floor_down()

    def floor_up(self):
        self.floor +=1
        print(f"Now it's on {self.floor}")

    def floor_down(self):
        self.floor -=1
        print(f"Now it's on {self.floor}")

class building:
    def __init__(self, bottom, top, elev_num):
        self.bottom = bottom
        self.top = top
        self.elevator_num = elev_num
        self.elevs = []
        for i in range(elev_num):
            self.elevs.append(elevator(bottom, top))

    def run_elevators(self, num, floor):
        self.elevs[num].go_to_floor(floor)


building = building(5, 15, elev_num=5)
building.run_elevators(4, 30)

########### Exercise 3 ###########
class elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.floor = bottom

    def go_to_floor(self, floor):
        if floor > self.floor:
            while floor > self.floor:
                self.floor_up()
        elif floor < self.floor:
            while floor < self.floor:
                self.floor_down()

    def floor_up(self):
        self.floor +=1
        print(f"Now it's on {self.floor}")

    def floor_down(self):
        self.floor -=1
        print(f"Now it's on {self.floor}")

class building:
    def __init__(self, bottom, top, elev_num):
        self.bottom = bottom
        self.top = top
        self.elevator_num = elev_num
        self.elevs = []
        for i in range(elev_num):
            self.elevs.append(elevator(bottom, top))

    def run_elevators(self, num, floor):
        self.elevs[num].go_to_floor(floor)

    def fire_alarm(self):
        for i in self.elevs:
            i.go_to_floor(self.bottom)

building = building(5, 15, elev_num=5)
building.run_elevators(4, 20)
building.fire_alarm()

########### Exercise 4 ###########
import random
from tabulate import tabulate

class car:
    def __init__(self,reg_num,max_spd,cur_spd=0,distance=0):
        self.reg_num = reg_num
        self.max_spd = max_spd
        self.cur_spd = cur_spd
        self.distance = distance

    def prop(self):
        print(f"Registration Number: {self.reg_num}\nMax Speed: {self.max_spd}\nCurrent Speed: {self.cur_spd}\nDistance: {self.distance}")

    def accelerate(self, speed):
        self.cur_spd += speed
        if self.cur_spd > self.max_spd:
            self.cur_spd = self.max_spd
        if self.cur_spd < 0:
            self.cur_spd = 0

    def drive(self,time):
        self.distance += time * self.cur_spd

class race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for i in cars:
            i.accelerate(random.randint(-10, 15))
            i.drive(1)

    def race_finished(self):
        finished = False
        for i in cars:
            if i.distance > self.distance:
                finished = True
        return finished

    def print_status(self):
        headers = ["Cars", "Speed", "Distance"]
        mydata = []
        for i in self.cars:
            mydata.append([i.reg_num, i.cur_spd, i.distance])
        print(tabulate(mydata, headers=headers, tablefmt="grid"))


cars = []
for i in range(0,10):
    cars.append("")
    cars[i]= car(f"ABC-{i+1}",random.randint(100,200))

race = race('Grand Demolition Derby', 8000, cars)
time =0
while (race.race_finished()!=True):
    race.hour_passes()
    time+=1
    if(time == 10):
        race.print_status()
        time=0

race.print_status()
print('The race has finished!')