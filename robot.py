import dinosaur
from weapon import Weapon

class Robot:
  def __init__(self, name):
    self.name
    self.health = 100
    self.weapon : Weapon = None
    self.is_alive = True

  def take_damage(self, amount):
    self.health -= amount
    self.checkHealth()
  
  def attack(self, dinosaur):
    dinosaur.take_damage(self.weapon.attack_power)

  def checkHealth(self):
    self.is_alive = False if self.health <= 0 else True

  