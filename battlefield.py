from fleet import Fleet
from herd import Herd

from helpers import type_msg_slowly, validate_int_input
from constants import COMBAT_MENU, INTRO_MSG, MAIN_MENU

class Battlefield:
  def __init__(self):
    self.player = None
    self.ai = None
  
  def run_game(self):
    # self._display_intro()
    self._run_main_menu()

  def battle(self):
    pass

  def _initial_player_turn(self):
    self.player.display_begin_battle_msg()
    self.player_turn()
  
  def player_turn(self):
    self._display_combat_options()

  def ai_turn(self):
    pass

  def check_for_winner(self): # FIXME: implement conditionals
    if(self.player.check_if_defeated()):
      pass
    elif(self.ai.check_if_defeated()):
      pass
    else:
      pass

  def _display_combat_options(self):
    prompt = COMBAT_MENU
    while True:
      self.player.display_status()
      userInput = validate_int_input(prompt)

      match userInput:
        case 1:
          self.player.select_targets(self.ai)
        case 2: # engage opponent
          pass # implement player turn method followed by AI turn method
        case 3: # surrender
          return
        case _:
          prompt = 'Please select between 1-3'
    
  def _select_player_targets(self):
    self.player

  def display_winners(self):
    pass  

  def _display_intro(self):
    type_msg_slowly(INTRO_MSG)

  def _run_main_menu(self):
    prompt = MAIN_MENU
    while True:
      user_input = validate_int_input(prompt)
      match user_input:
        case 1:
          self._init_player_fleet()
        case 2:
          self._init_player_herd()
        case 3:
          print("Now we'll never know the fate of the planet...\n")
          exit()
        case _:
          prompt = 'Please choose 1-3: '

  def _init_player_fleet(self):
    self.player = Fleet()
    self.ai = Herd(True)
    self._initial_player_turn()

  def _init_player_herd(self):
    self.player = Herd()
    self.ai = Fleet(True)
    self._initial_player_turn()