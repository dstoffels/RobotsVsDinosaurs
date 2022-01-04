import random
import time
from constants import BEGIN_BATTLE_MSG_ROBOT, NUM_COMBATANTS
from helpers import display_viable_targets, index_len, text_crawler, validate_index_input
from robot import ROBOTS, Robot
from weapon import WEAPONS

class Fleet:
  def __init__(self, is_AI=False):
    self.robots: list[Robot] = []
    self.is_AI = is_AI

    if(self.is_AI):
      self.create_random_fleet()
    else:
      self.create_fleet()

  def display_begin_battle_msg(self):
    text_crawler(BEGIN_BATTLE_MSG_ROBOT)

  def is_defeated(self):
    dead_robots = 0
    for robot in self.robots:
      dead_robots += 1 if robot.health <= 0 else 0
    if(dead_robots == 3):
      return True
    else:
      return False

  def attack(self, opponent):
    if self.is_AI:
      self.select_targets(opponent)
      print('The enemy fleet attacks the herd!\n')
      self._attack_targets()
    else:
      if self.attack_is_valid():
        print('Your fleet attacks the enemy herd!\n')
        self._attack_targets()
      else:
        print('Your fleet needs targets first!\n')
        time.sleep(1)

  def _attack_targets(self):
    for robot in self.robots:
      robot.attack(robot.target)

  def attack_is_valid(self):
    for robot in self.robots:
      if not robot.target:
        return False
    return True

  def select_targets(self, opponent):
    viable_targets = self._filter_living_targets(opponent.dinosaurs)
    if self.is_AI:
      self._select_random_targets(viable_targets)
    else:
      for robot in self.robots:
        prompt = f'\nChoose a target for {robot.name}: '
        display_viable_targets(viable_targets)
        i = validate_index_input(prompt, viable_targets)
        robot.target = viable_targets[i]
        print(f'{robot.name} is now targeting {robot.target.name}\n')
  
  def _select_random_targets(self, targets):
    for robot in self.robots:
      i = random.randint(0, index_len(targets))
      robot.target = targets[i]
      targets.pop(i)

  def _filter_living_targets(self, dinosaurs):
    targets = []
    for dino in dinosaurs:
      if dino.is_alive:
        targets.append(dino)
    return targets

  def display_status(self):
    for robot in self.robots:
      if robot.is_alive:
        target = f'{robot.target.name} | Target Health: {robot.target.health}' if robot.target else 'None'
        print(f'[{robot.name} | Health: {robot.health}]  [Target: {target}]')
      else:
        print(f'[{robot.name}: OFFLINE]')

  def create_fleet(self):
    self.robots.clear()
    name_prompt = f"Enter your robit's designation: "
    weapons = WEAPONS.copy()

    i = 0
    while i < NUM_COMBATANTS:
      name = input(name_prompt)
      new_robot = Robot(name)
      new_robot.equip_weapon(weapons)
      self.robots.append(new_robot)
      i += 1

  # may update this to randomly generate 8-bit binary strings for robot names instead of pulling from ROBOTS
  def create_random_fleet(self):
    robots = ROBOTS.copy()
    weapons = WEAPONS.copy()
    for robot in robots:
      robot.select_random_weapon(weapons)
      self.robots.append(robot)

