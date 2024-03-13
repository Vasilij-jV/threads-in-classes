# -*- config: utf8 -*-

import random
from collections import defaultdict
from threading import Thread, Lock
from time import sleep

mutex = Lock()


class Citadel(Thread):

    def __init__(self, name, skill, *args, **kwargs):
        super(Citadel, self).__init__(*args, **kwargs)
        self.str_day = None
        self.name = name
        self.skill = skill
        self.enemies = 100
        self.num_day = 0

    def run(self):
        print(f'Sir {self.name} на нас напали!')
        for number in range(11):
            sleep(1)
            with mutex:
                if self.enemies > 0:
                    self.num_day += 1
                    self.enemies -= self.skill
                    if self.num_day == 1:
                        self.str_day = 'день'
                        print(
                            f'Sir {self.name} сражается {self.num_day} {self.str_day}..., осталось {self.enemies} воинов')
                    elif 1 < self.num_day < 5:
                        self.str_day = 'дня'
                        print(
                            f'Sir {self.name} сражается {self.num_day} {self.str_day}..., осталось {self.enemies} воинов')
                    if self.num_day > 4:
                        self.str_day = 'дней'
                        print(
                            f'Sir {self.name} сражается {self.num_day} {self.str_day}..., осталось {self.enemies} воинов')
                if self.enemies == 0:
                    print(f'Sir {self.name} одержал победу спустя {self.num_day} дней!\n')
                    break


percival = Citadel('Percival', 20)
bors = Citadel('Bors', 10)

percival.start()
bors.start()

percival.join()
bors.join()
