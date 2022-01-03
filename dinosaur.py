from robot import Robot

class Dinosaur:
  def __init__(self, name, attack_power):
    self.name: str = name
    self.attack_power: int = attack_power
    self.health: int = 100

  def attack(self, robot: Robot):
    pass