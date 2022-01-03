import random
from dinosaur import Dinosaur, DINOSAURS
from constants import NUM_COMBATANTS
from helpers import choose_dino_from_list

class Herd:
  def __init__(self):
    self.dinosaurs: list[Dinosaur] = []

  def display_herd_info(self):
    for dino in self.dinosaurs:
      print(f'{dino.name}: [Health: {dino.health}]')

  def create_herd(self):
    self.dinosaurs.clear()
    dino_list = DINOSAURS.copy()

    i = 0
    while i < NUM_COMBATANTS:
      new_dino = choose_dino_from_list(dino_list)
      self.dinosaurs.append(new_dino)
      i += 1
      
  def create_random_herd(self):
    dinosaurs = DINOSAURS.copy()
    i = 0
    while i < NUM_COMBATANTS:
      index = random.randint(0, len(dinosaurs) - 1)
      self.dinosaurs.append(dinosaurs[index])
      dinosaurs.pop(index)
      i += 1