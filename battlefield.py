from fleet import Fleet
from herd import Herd
from dinosaur import Dinosaur
from robot import Robot

from helpers import type_msg_slowly, validate_int_input
from constants import COMBAT_MENU, INTRO_MSG, MAIN_MENU

class Battlefield:
  def __init__(self):
    self.fleet: Fleet = None
    self.herd: Herd = None
  
  def run_game(self):
    pass

  def display_welcome(self):
    type_msg_slowly(INTRO_MSG)
    self._display_main_menu()

  def _display_main_menu(self):
    prompt = MAIN_MENU

    while True:
      user_input = validate_int_input(prompt)
      match user_input:
        case 1:
          self.fleet = Fleet()
          self.herd = Herd(True)
          self.display_combat_options()
        case 2:
          self.herd = Herd()
          self.fleet = Fleet(True)
          self.display_combat_options()
        case 3:
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

  # FIXME: implement conditionals
  def check_for_winner(self):
    if(self.herd.check_if_defeated()):
      pass
    elif(self.fleet.check_if_defeated()):
      pass
    else:
      pass

  def display_combat_options(self):
    prompt = COMBAT_MENU
    while True:
      userInput = validate_int_input(prompt)

      match userInput:
        case 1:
          pass # implement target selection method
        case 2:
          pass # implement player turn method followed by AI turn method
        case 3:
          return
        case _:
          prompt = 'Please select between 1-3'

  def display_winners(self):
    pass  



