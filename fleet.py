from constants import NUM_COMBATANTS
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

  def check_if_defeated(self):
    dead_robots = 0
    for robot in self.robots:
      dead_robots += 1 if robot.health <= 0 else 0
    if(dead_robots == 3):
      return True
    else:
      return False  

  def display_fleet_info(self):
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

  # may update this to randomly generate 8-bit binary strings for robot names
  def create_random_fleet(self):
    robots = ROBOTS.copy()
    weapons = WEAPONS.copy()
    for robot in robots:
      robot.select_random_weapon(weapons)
      self.robots.append(robot)

