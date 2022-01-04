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
    self.checkHealth()

  def set_target(self, robot):
    self.target = robot

  def attack(self, robot):
    damage = self.attack_power + random.randint(-5, 5)
    robot.take_damage(damage)
    print(f'{self.name} attacks {robot.name} for {damage} damage!\n')
    time.sleep(0.7)

  def checkHealth(self):
    self.is_alive = False if self.health <= 0 else True

PACHYCEPHELASAURUS = Dinosaur('Pachycephalosaurus', 10)
TRICERATOPS = Dinosaur('Triceratops', 15)
PROCOMPSOGNATHUS = Dinosaur('Procompsognathus', 20)
TYRANNOSAURUS_REX = Dinosaur('Tyrannosaurus Rex', 15)
VELOCIRAPTOR = Dinosaur('Velociraptor', 10)

DINOSAURS = [PACHYCEPHELASAURUS, TRICERATOPS, PROCOMPSOGNATHUS, TYRANNOSAURUS_REX, VELOCIRAPTOR]