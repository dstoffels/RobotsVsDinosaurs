from fleet import Fleet
from herd import Herd

from helpers import text_crawler, validate_index_input, validate_int_input
from constants import COMBAT_MENU, INTRO_MSG, MAIN_MENU, PLAY_AGAIN

class Battlefield:
  def __init__(self):
    self.player = None
    self.ai = None
    self.game_over = True
    self.player_attacks_first = True

  def start(self):
    self._display_intro()
    self._run_main_menu()
  
  def run_game(self):
    self.game_over = False
    self.player.display_begin_battle_msg()
    self._display_combat_options()

  def _battle(self):
    if not self.player.attack_is_valid(): return
    if self.player_attacks_first:
      self.player_turn()
      if not self.game_over: self.ai_turn()
    else:
      self.ai_turn()
      if not self.game_over: self.player_turn()
    self._toggle_first_attacker()

  def player_turn(self):
    self.player.attack(self.ai)
    self.check_for_winner()

  def ai_turn(self):
    self.ai.attack(self.player)
    self.check_for_winner()

  def check_for_winner(self):
    if self.player.is_defeated(): self._defeat()
    elif self.ai.is_defeated(): self._victory()

  def _victory(self):
    self.player.victory()
    self.end_game()

  def _defeat(self):
    self.player.defeat()
    self.end_game()

  def end_game(self):
    self.player = self.ai = None
    self.game_over = True

  def _toggle_first_attacker(self):
    self.player_attacks_first = not self.player_attacks_first

  def _display_combat_options(self):
    while not self.game_over:
      self.player.display_status()

      prompt = COMBAT_MENU
      userInput = validate_int_input(prompt)
      match userInput:
        case 1: self._select_player_targets()
        case 2: self._battle()
        case 3: self._defeat() # surrender
        case _: prompt = 'Please select between 1-3'
    
    userInput = validate_int_input(PLAY_AGAIN)
    match userInput:
      case 1: return
      case 2: exit()
    
  def _select_player_targets(self):
    self.player.select_targets(self.ai)


  def _display_intro(self):
    text_crawler(INTRO_MSG)

  def _run_main_menu(self):
    prompt = MAIN_MENU
    while True:
      user_input = validate_int_input(prompt)
      match user_input:
        case 1: self._init_player_fleet()
        case 2: self._init_player_herd()
        case 3:
          print("Now we'll never know the fate of the planet...\n")
          exit()
        case _: prompt = 'Please choose 1-3: '

  def _init_player_fleet(self):
    self.player = Fleet()
    self.ai = Herd(True)
    self.run_game()

  def _init_player_herd(self):
    self.player = Herd()
    self.ai = Fleet(True)
    self.run_game()