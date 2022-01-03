import robot

class Dinosaur:
  def __init__(self, name, attack_power):
    self.name: str = name
    self.attack_power: int = attack_power
    self.health: int = 100
    self.is_alive = True

  def take_damage(self, amount):
    self.health -= amount
    self.checkHealth()

  def attack(self, robot):
    robot.take_damage(self.attack_power)

  def checkHealth(self):
    self.is_alive = False if self.health <= 0 else True