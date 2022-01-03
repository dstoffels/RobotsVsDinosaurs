class Weapon:
  def __init__(self, name, attack_power):
    self.name = name
    self.attack_power = attack_power

ROBO_SWORD = Weapon('Robo Sword', 10)
ELECTRO_PROD = Weapon('Electro Prod', 15)
GAMMA_LASER = Weapon('Gamma Laser', 20)

WEAPONS = [ROBO_SWORD, ELECTRO_PROD, GAMMA_LASER]
