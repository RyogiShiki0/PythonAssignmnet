########### Exercise 1 ###########
class publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f'Name: {self.name}')

class book(publication):
    def __init__(self, name, author, page_count):
        self.page_count = page_count
        self.author = author
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f'Author: {self.author}')
        print(f'Page Count: {self.page_count}')

class magazine(publication):
    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f'Editor: {self.editor}')

publication = []
publication.append(magazine('Donald Duck', 'Aki Hyyppä'))
publication.append(book('Compartment No. 6', 'Rosa Liksom', 192))
for i in publication:
    i.print_info()

########### Exercise 2 ###########
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

class electric_car(car):
    def __init__(self,reg_num,max_spd,battery,cur_spd=0,distance=0):
        self.battery = battery
        super().__init__(reg_num,max_spd,cur_spd,distance)

class gasonline_car(car):
    def __init__(self,reg_num,max_spd,tank,cur_spd=0,distance=0):
        self.tank = tank
        super().__init__(reg_num,max_spd,cur_spd,distance)

car1=electric_car("ABC-15",180,52.5)
car2=gasonline_car("ACD-123",165,32.3)
car1.accelerate(55)
car2.accelerate(50)
car1.drive(3)
car2.drive(3)
print(f"The distance of Car1 is {car1.distance},The distance of Car2 is {car2.distance}")