import random
import time
import copy

from dinosaur import Dinosaur, DINOSAURS
from constants import BEGIN_BATTLE_MSG_DINO, HERD_DEFEAT, HERD_VICTORY, NUM_COMBATANTS
from helpers import choose_dino_from_list, display_viable_targets, index_len, text_crawler, validate_index_input

class Herd:
  def __init__(self, is_AI = False):
    self.dinosaurs: list[Dinosaur] = []
    self.is_AI = is_AI

    if(self.is_AI):
      self.create_random_herd()
    else:
      self.create_herd()

  def display_begin_battle_msg(self):
    text_crawler(BEGIN_BATTLE_MSG_DINO)

  def is_defeated(self):
    dead_dinos = 0
    for dino in self.dinosaurs:
      dead_dinos += 1 if dino.health <= 0 else 0
    if(dead_dinos == 3):
      return True
    else:
      return False
  
  def attack(self, opponent):
    if self.is_AI:
      self.select_targets(opponent)
      print('***The enemy herd attacks the fleet!***\n')
      self._attack_targets(opponent)
    else:
      if self.attack_is_valid():
        print('***Your herd attacks the enemy fleet!***\n')
        self._attack_targets(opponent)

  def _attack_targets(self, opponent):
      for dino in self.dinosaurs:
        if dino.is_alive:
          dino.attack()
          if opponent.is_defeated(): break

  def attack_is_valid(self):
    for dino in self.dinosaurs:
      if not dino.target:
        print('***Your herd needs targets first!***\n')
        time.sleep(1)
        return False
    return True

  def clear_dead_targets(self):
    for dino in self.dinosaurs:
      if not dino.target_is_alive():
        dino.clear_target()

  def select_targets(self, opponent):
    viable_targets = self._filter_living_targets(opponent.robots)
    if self.is_AI:
      self._select_random_targets(viable_targets)
    else:
      self._manual_target_select(viable_targets)

  def _manual_target_select(self, targets):
    for dino in self.dinosaurs:
      if dino.is_alive:
        prompt = f'\nChoose a target for {dino.name}: '
        display_viable_targets(targets)
        i = validate_index_input(prompt, targets)
        dino.set_target(targets[i])
        print(f'{dino.name} is now targeting {dino.target.name}\n')

  def _select_random_targets(self, targets):
    for dino in self.dinosaurs:
      i = random.randint(0, index_len(targets))
      dino.target = targets[i]

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
    dino_list = copy.deepcopy(DINOSAURS)

    i = 0
    while i < NUM_COMBATANTS:
      new_dino = choose_dino_from_list(dino_list)
      self.dinosaurs.append(new_dino)
      i += 1
      
  def create_random_herd(self):
    dinosaurs = copy.deepcopy(DINOSAURS)
    
    i = 0
    while i < NUM_COMBATANTS:
      index = random.randint(0, index_len(dinosaurs))
      self.dinosaurs.append(dinosaurs[index])
      dinosaurs.pop(index)
      i += 1

  def victory(self):
    text_crawler(HERD_VICTORY)
  
  def defeat(self):
    text_crawler(HERD_DEFEAT)