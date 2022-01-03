from weapon import WEAPONS

NUM_COMBATANTS = 3

MAIN_MENU = '''
Choose your side:
1) Robots
2) Dinosaurs

'''



def display_menu_return_rob_or_dino():
    prompt = MAIN_MENU

    while True:
      user_input = input(prompt)
      match user_input:
        case '1':
          return # run robot prompt
        case '2':
          return # run dinosaur prompt
        case _:
          prompt = 'Please choose 1-2: '

def display_robot_menu():
  variant = ''
  name_prompt = f'Name your {variant}robot'

  i = 0
  while i < NUM_COMBATANTS:
    name = input(name_prompt)
    weapon_index = input(choose_weapon_str_builder(name))
    i += 1
    variant = 'next '

def choose_weapon_str_builder(name):
  string = f'''
Choose a weapon for {name}: 
'''
  i = 1
  for weapon in WEAPONS:
    string += f'{i}) {weapon.name}\n'
    i += 1
  return string