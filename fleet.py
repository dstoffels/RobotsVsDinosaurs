from constants import NUM_COMBATANTS
from helpers import choose_weapon_str_builder
from robot import Robot
from weapon import WEAPONS

class Fleet:
  def __init__(self):
    self.robots: list[Robot] = []

  def create_fleet(self, for_AI=False):
    if(for_AI):
      self.create_random_fleet()
    else:
      variant = 'first '
      name_prompt = f'Name your {variant}robot'
      i = 0
      while i < NUM_COMBATANTS:
        name = input(name_prompt)
        weapon_index = int(input(choose_weapon_str_builder(name)))
        new_robot = Robot(name, WEAPONS[weapon_index])
        self.robots.append(new_robot)
        i += 1
        variant = 'next '


  def create_random_fleet(self):
    pass # setup random generation