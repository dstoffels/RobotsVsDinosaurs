import time
from helpers import choose_weapon_from_list, index_len
from weapon import Weapon, WEAPONS
import random

class Robot:
  def __init__(self, name):
    self.name = name
    self.health = 100
    self.weapon : Weapon = None
    self.is_alive = True
    self.target = None

  def equip_weapon(self, weapons):
      self.weapon = choose_weapon_from_list(self.name, weapons)      

  def select_random_weapon(self, weapons):
    i = random.randint(0, index_len(weapons))
    self.weapon = weapons[i]
    weapons.pop(i)

  def set_target(self, dino):
    self.target = dino
  
  def take_damage(self, amount):
    self.health -= amount
    self.checkHealth()
  
  def attack(self, dinosaur):
    damage = self.weapon.attack_power + random.randint(-5, 5)
    dinosaur.take_damage(damage)
    print(f'{self.name} attacks {dinosaur.name} for {damage} damage!\n')
    time.sleep(0.7)

  def checkHealth(self):
    self.is_alive = False if self.health <= 0 else True

  
  
DATA = Robot('Data')
DALEK = Robot('Dalek')
OMNITRON = Robot('Omnitron')

ROBOTS = [DATA, DALEK, OMNITRON]