from weapon import WEAPONS
def choose_weapon_str_builder(name):
  string = f'''
Choose a weapon for {name}: 
'''
  i = 1
  for weapon in WEAPONS:
    string += f'{i}) {weapon.name}\n'
    i += 1
  return string