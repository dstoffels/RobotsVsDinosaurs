from constants import MAIN_MENU
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
from robot import Robot
import time
import sys

class Battlefield:
  def __init__(self):
    self.fleet: Fleet = Fleet()
    self.herd: Herd = Herd()
  
  def run_game(self):
    # self.display_welcome()
    self.display_main_menu()

  def display_welcome(self):
    for char in INTRO_MSG:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(0.02)

  def display_main_menu(self):
    prompt = MAIN_MENU

    while True:
      user_input = input(prompt)
      match user_input:
        case '1':
          self.fleet.create_fleet()
          self.herd.create_herd(True)
          self.battle()
        case '2':
          self.herd.create_herd()
          self.fleet.create_fleet(True)
          self.battle()
        case _:
          prompt = 'Please choose 1-2: '

  def battle(self):
    pass

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

INTRO_MSG = '''It is the year 3040 and humans have long been extinct.
All that remains of the scorched Earth are the robots that destroyed them, and the dinosaurs they resurrected for theme parks.
The final battle between the Robots and the Dinosaurs has begun, you decide the fate of the planet!
'''

