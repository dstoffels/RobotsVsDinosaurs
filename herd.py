import random
from dinosaur import Dinosaur, DINOSAURS
from constants import BEGIN_BATTLE_MSG_DINO, NUM_COMBATANTS
from helpers import choose_dino_from_list, display_viable_targets, type_msg_slowly, validate_index_input

class Herd:
  def __init__(self, is_AI = False):
    self.dinosaurs: list[Dinosaur] = []
    self.is_AI = is_AI

    if(self.is_AI):
      self.create_random_herd()
    else:
      self.create_herd()

  def display_begin_battle_msg(self):
    type_msg_slowly(BEGIN_BATTLE_MSG_DINO)

  def check_if_defeated(self):
    dead_dinos = 0
    for dino in self.dinosaurs:
      dead_dinos += 1 if dino.health <= 0 else 0
    if(dead_dinos == 3):
      return True
    else:
      return False

  def select_targets(self, opponent):
    viable_targets = self._filter_living_targets(opponent.robots)
    if self.is_AI:
      self._select_random_targets(viable_targets)
    else:
      for dino in self.dinosaurs:
        prompt = f'\nChoose a target for {dino.name}: '
        display_viable_targets(viable_targets)
        i = validate_index_input(prompt, viable_targets)
        dino.target = viable_targets[i]
        print(f'{dino.name} is now targeting {dino.target.name}\n')
  
  def _select_random_targets(self, targets):
    for dino in self.dinosaurs:
      i = random.randint(0, len(targets))
      dino.target = targets[i]
      targets.pop(i)

  def _filter_living_targets(self, robots):
    targets = []
    for robot in robots:
      if robot.is_alive:
        targets.append(robot)
    return targets

  def display_status(self):
    for dino in self.dinosaurs:
      if dino.is_alive:
        target = f'{dino.target.name} | Target Health: {dino.target.health}' if dino.target else 'None'
        print(f'[{dino.name} | Health: {dino.health}] [Target: {target}]')
      else:
        print(f'[{dino.name}: EXTINCT]')

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