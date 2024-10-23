########### Exercise 1 ###########

class car:
    def __init__(self,reg_num,max_spd,cur_spd=0,distance=0):
        self.reg_num = reg_num
        self.max_spd = max_spd
        self.cur_spd = cur_spd
        self.distance = distance

    def prop(self):
        print(f"Registration Number: {self.reg_num}\nMax Speed: {self.max_spd}\nCurrent Speed: {self.cur_spd}\nDistance: {self.distance}")
car1 = car('ABC-123',142)
car1.prop()
########### Exercise 2 ###########
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
        print(f"Current Speed: {self.cur_spd}")

car1 = car('ABC-123',142)
car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
car1.accelerate(-200)

########### Exercise 3 ###########
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
        print(f"Current Speed: {self.cur_spd}")

    def drive(self,time):
        self.distance += time * self.cur_spd

car1 = car('ABC-123',142,0,2000)
car1.accelerate(60)
car1.drive(1.5)
car1.prop()
########### Exercise 4 ###########
import random
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

cars = []
for i in range(0,10):
    cars.append("")
    cars[i]= car(f"ABC-{i+1}",random.randint(100,200))

over = False
while(over != True):
    for i in range(0,10):
        cars[i].accelerate(random.randint(-10,15))
        cars[i].drive(1)
        if (cars[i].distance > 10000):
            over = True

for i in range(0,10):
    cars[i].prop()