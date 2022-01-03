from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
from robot import Robot


class Battlefield:
  def __init__(self):
    self.fleet: Fleet = None
    self.herd: Herd = None
  
  def run_game(self):
    pass

  def display_welcome(self):
    pass

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


