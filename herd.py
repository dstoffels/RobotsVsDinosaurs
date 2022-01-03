import random
from dinosaur import Dinosaur, DINOSAURS
from constants import NUM_COMBATANTS
from helpers import choose_dino_from_list

class Herd:
  def __init__(self, is_AI = False):
    self.dinosaurs: list[Dinosaur] = []
    self.is_AI = is_AI

    if(self.is_AI):
      self.create_random_herd()
    else:
      self.create_herd()

  def check_if_defeated(self):
    dead_dinos = 0
    for dino in self.dinosaurs:
      dead_dinos += 1 if dino.health <= 0 else 0
    if(dead_dinos == 3):
      return True
    else:
      return False  


  def display_herd_info(self):
    title = '\nENEMY HERD:' if self.is_AI else '\nYOUR HERD:'
    print(title)
    for dino in self.dinosaurs:
      target = dino.target.name if dino.target else 'None'
      target = f' | Target: {target}' if not self.is_AI else ''
      print(f'{dino.name}: [Health: {dino.health}{target}]')

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