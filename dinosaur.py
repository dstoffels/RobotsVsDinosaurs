import random
import time


class Dinosaur:
  def __init__(self, name, attack_power):
    self.name: str = name
    self.attack_power: int = attack_power
    self.health: int = 100
    self.is_alive = True
    self.target = None

  def take_damage(self, amount):
    self.health -= amount
    self._check_health()

  def set_target(self, robot):
    self.target = robot
  
  def clear_target(self):
    self.target = None

  def attack(self):
    if self.target_is_alive():
      self._damage_target()
    else:
      print(f'***{self.target.name} is already dead, attack canceled***\n')
      self.clear_target()
    time.sleep(0.7)

  def _damage_target(self):
    damage = self.attack_power + random.randint(-5, 5)
    print(f'{self.name} attacks {self.target.name} for {damage} damage!\n')
    self.target.take_damage(damage)
    if not self.target_is_alive():
      self.clear_target()

  def target_is_alive(self):
    if self.target.is_alive: return True
    else: return False

  def _check_health(self):
    if(self.health <= 0):
      self.is_alive = False
      print(f'***{self.name} has fallen on the battlefield!***\n')
    

PACHYCEPHELASAURUS = Dinosaur('Pachycephalosaurus', 10)
TRICERATOPS = Dinosaur('Triceratops', 15)
PROCOMPSOGNATHUS = Dinosaur('Procompsognathus', 20)
TYRANNOSAURUS_REX = Dinosaur('Tyrannosaurus Rex', 15)
VELOCIRAPTOR = Dinosaur('Velociraptor', 10)

DINOSAURS = [PACHYCEPHELASAURUS, TRICERATOPS, PROCOMPSOGNATHUS, TYRANNOSAURUS_REX, VELOCIRAPTOR]