import random
from dinosaur import Dinosaur, DINOSAURS
from constants import NUM_COMBATANTS
from helpers import choose_dino_from_list

class Herd:
  def __init__(self):
    self.dinosaurs: list[Dinosaur] = []
    self.is_AI = False

  def display_herd_info(self):
    title = '\nENEMY HERD: \n' if self.is_AI else '\nYOUR HERD: \n'
    print(title)
    for dino in self.dinosaurs:
      target = dino.target.name if dino.target else 'None'
      print(f'{dino.name}: [Health: {dino.health} | Target: {target}]')

  def create_herd(self):
    self.dinosaurs.clear()
    dino_list = DINOSAURS.copy()

    i = 0
    while i < NUM_COMBATANTS:
      new_dino = choose_dino_from_list(dino_list)
      self.dinosaurs.append(new_dino)
      i += 1
      
  def create_random_herd(self):
    self.is_AI = True
    self.dinosaurs.clear()
    dinosaurs = DINOSAURS.copy()
    i = 0
    while i < NUM_COMBATANTS:
      index = random.randint(0, len(dinosaurs) - 1)
      self.dinosaurs.append(dinosaurs[index])
      dinosaurs.pop(index)
      i += 1