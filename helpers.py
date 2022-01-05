import time
import sys

def choose_weapon_from_list(name, weapons: list):
  prompt = choose_weapon_str_builder(name, weapons)
  i = validate_index_input(prompt, weapons)
  weapon = weapons[i]
  weapons.pop(i)
  return weapon

def choose_dino_from_list(dinosaurs: list):
  prompt = choose_dino_str_bldr(dinosaurs)
  i = validate_index_input(prompt, dinosaurs)
  dino = dinosaurs[i]
  dinosaurs.pop(i)
  return dino

def choose_weapon_str_builder(name, weapons):
  string = f'''
Choose a weapon for {name}: 
'''
  i = 1
  for weapon in weapons:
    string += f'{i}) {weapon.name}\n'
    i += 1
  return string + '\n'

def choose_dino_str_bldr(dinosaurs):
  string = f'''
Choose a dinosaur for your herd: 
'''
  i = 1
  for dino in dinosaurs:
    string += f'{i}) {dino.name}\n'
    i += 1
  return string + '\n'

def text_crawler(message):
  for char in message:
    pause = 0.02
    if(char == '\n'):
      pause = 0.7
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(pause)

def validate_int_input(prompt):
  while True:
    try:
      response = int(input(prompt))
      return response
    except:
      prompt = 'Please enter a number: '

def validate_index_input(prompt, list):
  response = validate_int_input(prompt)
  while response > len(list) or response < 0:
    prompt = f'Please select a number between 1-{len(list)}: '
    response = validate_int_input(prompt)
  return response - 1

def display_viable_targets(targets):
  print('Available Targets:')
  i = 1
  for target in targets:
    print(f'{i}) {target.name} | Health: {target.health}')
    i += 1

def index_len(list):
  return len(list) - 1