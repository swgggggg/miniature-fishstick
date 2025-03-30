import random


class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 500
        self.alive = True

    def to_study(self):
        print('Time to study...')
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print('Time to sleep')
        self.gladness += 3

    def to_chill(self):
        print('Rest time')
        self.progress += 0.1
        self.gladness += 5

    def is_alive(self):
        if self.progress < -0.5:
            print('Failed...')
            self.alive = False
        elif self.gladness <= 0:
            print('Depression...')
            self.alive = False
        elif self.progress > 5:
            print('Genius...')
            self.alive = False

    def end_of_day(self):
        print(f'Gladness - {self.gladness}')
        print(f'Progress - {self.progress}')

    def live(self, day):
        print(f'Day {day} of {self.name} life')
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        else:
            self.to_chill()

        self.end_of_day()
        self.is_alive()



class Motorcycle(Student):

    def __init__(self, brand):
        self.brand = brand

    def to_repair(self):
        print('Repair')
        self.progress += 0.12

    def to_fill(self):
        print('Fill')
        self.money -= 25

    def to_clean(self):
        print('Clean')
        self.progress += 1
        self.money -= 5
        self.gladness -= 0.5


nick = Student(name='Nick')
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)