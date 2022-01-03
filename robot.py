from helpers import choose_weapon_from_list
from weapon import Weapon
import random

class Robot:
  def __init__(self, name):
    self.name = name
    self.health = 100
    self.weapon : Weapon = None
    self.is_alive = True

  def equip_weapon(self, weapons):
      self.weapon = choose_weapon_from_list(self.name, weapons)      

  def select_random_weapon(self, weapons):
    i = random.randint(0,len(weapons) - 1)
    weapon = weapons[i]
    weapons.pop(i)
    return weapon


  def take_damage(self, amount):
    self.health -= amount
    self.checkHealth()
  
  def attack(self, dinosaur):
    dinosaur.take_damage(self.weapon.attack_power)

  def checkHealth(self):
    self.is_alive = False if self.health <= 0 else True

  
  
DATA = Robot('Data')
DALEK = Robot('Dalek')
OMNITRON = Robot('Omnitron')

ROBOTS = [DATA, DALEK, OMNITRON]