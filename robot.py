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
  
  def clear_target(self):
    self.target = None
  
  def take_damage(self, amount):
    self.health -= amount
    self.checkHealth()
  
  def attack(self):
    if self.target_is_alive():
      self._damage_target()
    else:
      print(f'***{self.target.name} is already dead, attack canceled***\n')
      self.clear_target()
    time.sleep(0.7)

  def _damage_target(self):
    damage = self.weapon.attack_power + random.randint(-5, 5)
    print(f'{self.name} attacks {self.target.name} for {damage} damage!\n')
    self.target.take_damage(damage)
    if not self.target_is_alive():
      self.clear_target()

  def target_is_alive(self):
    if self.target.is_alive: return True
    else: return False

  def checkHealth(self):
    if(self.health <= 0):
      self.is_alive = False
      print(f'***{self.name} has fallen on the battlefield!***\n')

  
  
DATA = Robot('Data')
DALEK = Robot('Dalek')
OMNITRON = Robot('Omnitron')

ROBOTS = [DATA, DALEK, OMNITRON]