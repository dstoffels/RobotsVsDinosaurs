from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
from menu import display_menu
from robot import Robot
import time
import sys

class Battlefield:
  def __init__(self):
    self.fleet: Fleet = None
    self.herd: Herd = None
  
  def run_game(self):
    # self.display_welcome()
    display_menu()

  def display_welcome(self):
    for char in INTRO_MSG:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(0.02)

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

