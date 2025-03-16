import random


class Dog:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_play(self):
        print('Time to play')
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print('Time to sleep')
        self.gladness += 3

    def to_eat(self):
        print('eat time')
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
            print('To much food...')
            self.alive = False

    def end_of_day(self):
        print(f'Gladness - {self.gladness}')
        print(f'Progress - {self.progress}')

    def live(self, day):
        print(f'Day {day} of {self.name} life')
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_play()
        elif live_cube == 2:
            self.to_sleep()
        else:
            self.to_eat()

        self.end_of_day()
        self.is_alive()


spooky = Dog(name='Spooky')
for day in range(365):
    if spooky.alive == False:
        break
    spooky.live(day)