from constants import INTRO_MSG, MAIN_MENU
from dinosaur import Dinosaur
from fleet import Fleet
from helpers import type_msg_slowly
from herd import Herd
from robot import Robot

class Battlefield:
  def __init__(self):
    self.fleet: Fleet = Fleet()
    self.herd: Herd = Herd()
  
  def run_game(self):
    pass

  def display_welcome(self):
    type_msg_slowly(INTRO_MSG)
    self._display_main_menu()

  def _display_main_menu(self):
    prompt = MAIN_MENU

    while True:
      user_input = input(prompt)
      match user_input:
        case '1':
          self.fleet.create_fleet()
          self.herd.create_random_herd()
          self.battle()
        case '2':
          self.herd.create_herd()
          self.fleet.create_random_fleet()
          self.battle()
        case '3':
          print("Now we'll never know the fate of the planet...\n")
          exit()
        case _:
          prompt = 'Please choose 1-3: '

  def battle(self):
    if(self.herd.is_AI):
      self.fleet.display_fleet_info()
      self.herd.display_herd_info()
    else:
      self.herd.display_herd_info()
      self.fleet.display_fleet_info()

  def dino_turn(self, dinosaur: Dinosaur):
    pass

  def robot_turn(self, robot: Robot):
    pass

  def show_dino_opponent_options(self):
    pass

  def show_robot_opponent_options(self):
    pass

  def display_winners(self):
    pass  



