class Unit:
    def __init__(self):
        print("Unit creator")

class Flyable:
    def __init__(self):
        print("Flyable creator")

class FlyableUnit(Flyable,Unit):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)


dropship=FlyableUnit()

