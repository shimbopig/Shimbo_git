from stat import SF_APPEND
from unicodedata import name


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp =hp
        self.speed = speed

    def move(self, direction):
        print("[land unit moving]")
        print("{0} : {1} driection move".format(self.name, direction))
        print ("{0} unit is created".format(self.name))



class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} direction attack. damage {2}".format(self.name, \
            location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} damaged".format(self.name, damage))
        self.hp -=  damage
        print("{0} : current hp is {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} is destroyed".format(self.name))

firebat1 = AttackUnit("firebat",50,16,20)
firebat1.attack("east")

firebat1.damaged(30)
firebat1.damaged(30)

class Flyable:      #flying unit
    def __init__(self, flying_speed):
        self.flying_speed= flying_speed

    def fly(self, name, direction):
        print("{0} : flying {1} direction in {2}speed".format(name, direction, \
            self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

#Valkyrie
valkyrie = FlyableAttackUnit("Valkyrie", 200, 10, 6)
valkyrie.fly(valkyrie.name, "west")

vulture =  AttackUnit("Vulture", 80, 10, 20)

balltecruise = FlyableAttackUnit("battlecruiser",500,20,10)

vulture.move("South")
balltecruise.fly("ship","east")