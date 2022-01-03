from constants import NUM_COMBATANTS
from robot import ROBOTS, Robot
from weapon import WEAPONS

class Fleet:
  def __init__(self):
    self.robots: list[Robot] = []
    self.is_AI = False

  def display_fleet_info(self):
    title = '\nENEMY FLEET: \n' if self.is_AI else '\nYOUR FLEET: \n'
    print(title)
    for robot in self.robots:
      target = robot.target.name if robot.target else 'None'
      print(f'{robot.name}: [Health: {robot.health} | Target: {target}]')

  def create_fleet(self):
    self.robots.clear()
    name_prompt = f'Name your robot: '
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
    self.is_AI = True
    self.robots.clear()
    robots = ROBOTS.copy()
    weapons = WEAPONS.copy()
    for robot in robots:
      robot.select_random_weapon(weapons)
      self.robots.append(robot)

