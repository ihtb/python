# -*- coding:utf-8 -*-

class Creature:
    def __init__(self, sex):
        self.sex = sex

class Human(Creature):
    def __init__(self, sex, name):
        Creature.__init__(self, sex)
        self.name = name

Kita = Human("Man", "Kita Seigo")
print Kita.sex
print Kita.name
