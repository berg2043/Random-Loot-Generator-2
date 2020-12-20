import random
import numpy as np
import pandas as pd
import json

# Creates dictionaries that uses dice_dict as keys 
# dict[1] would return the pair for the range that include that key
class RangeDict(dict):
    def __getitem__(self, item):
        if not isinstance(item, range):
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item) 

# Globals
with open('items.json', 'r') as raw_item_db:
  item_db = json.load(raw_item_db)
challenge_rating_dict_raw = { 
  range(0, 5): 'CR 0-4',
  range(5, 11): 'CR 5-10',
  range(11, 17): 'CR 11-16',
  range(17, 50): 'CR 17+'
}
challenge_rating_dict = RangeDict(challenge_rating_dict_raw)

# Does currency for individual loot
def individual_currency(group_loot_dict, roll):
  cp_dice_to_roll = dict_creator(group_loot_dict["CP"])[roll]
  sp_dice_to_roll = dict_creator(group_loot_dict["SP"])[roll]
  ep_dice_to_roll = dict_creator(group_loot_dict["EP"])[roll]
  gp_dice_to_roll = dict_creator(group_loot_dict["GP"])[roll]
  pp_dice_to_roll = dict_creator(group_loot_dict["PP"])[roll]
  coins =[
    str(dice_roller(cp_dice_to_roll)) + " CP",
    str(dice_roller(sp_dice_to_roll)) + " SP",
    str(dice_roller(ep_dice_to_roll)) + " EP",
    str(dice_roller(gp_dice_to_roll)) + " GP",
    str(dice_roller(pp_dice_to_roll)) + " PP"
  ]
  return coins

# Rolls the dice and does the math
def dice_roller(dice_string):
  if dice_string == 0:
    return(0)
  else:
    number_of_dice = int(dice_string[0:dice_string.find('d')])
    dice_type = int(dice_string[dice_string.find('d')+1:dice_string.find('x')])
    multiplier = int(dice_string[dice_string.find('x')+1:])
    x = 0
    count = 0
    while x < number_of_dice:
      x += 1
      count += random.randint(1,dice_type)
    return(count*multiplier)

# Returns Gems and/or Art Objects
def art_and_gem(group_loot_dict,roll):
  art_and_gem_num_dict = dict_creator(group_loot_dict['GA Numb'])
  art_or_gems = []
  if art_and_gem_num_dict[roll] != 0:
    num_art_or_gems = dice_roller(art_and_gem_num_dict[roll])
    x = 0
    dice_dict = item_db['Gem Art Ranges']['Max']
    art_or_gem_dict = dict_creator(group_loot_dict['Gems or Art'])
    result_dict = item_db[art_or_gem_dict[roll]]['Item']
    while x < num_art_or_gems:
      rolls = random.randint(1, dice_dict[art_or_gem_dict[roll]])
      art_or_gems.append(f'{art_or_gem_dict[roll]}: {result_dict[str(rolls)]}')
      x += 1 
  return art_or_gems

# Retruns Magic Items
## Recieved a KeyError when a magic item wasn't rolled.  Used try to prevent.
def magic_items(group_loot_dict, roll):
  magic_item_num_dict = dict_creator(group_loot_dict['MI Numb'])
  magic_item2_num_dict = dict_creator(group_loot_dict['MI Numb 2'])
  items = []
  if magic_item_num_dict[roll] != 0:
    num_magic_items = dice_roller(magic_item_num_dict[roll])
    x = 0
    magic_item1_table = item_db[dict_creator(group_loot_dict['Item'])[roll]]
    magic_item1_table_dict = dict_creator(magic_item1_table['Item'])
    while x < num_magic_items:
      rolls = random.randint(1,100)
      items.append(magic_item1_table_dict[rolls])
      x += 1
  if magic_item2_num_dict[roll] != 0:
    num_magic_items2 = dice_roller(magic_item2_num_dict[roll])
    y = 0
    magic_item2_table = item_db[dict_creator(group_loot_dict['Item 2'])[roll]]
    magic_item2_table_dict = dict_creator(magic_item2_table['Item'])
    while y < num_magic_items2:
      rolls = random.randint(1,100)
      items.append(magic_item2_table_dict[rolls])
      y += 1
  return items

# Keys were strings and I couldn't figure out another way to turn them into dice_dict  
def dict_creator(raw_string_dict):
  new_dict = {}
  for key in raw_string_dict:
    new_dict[eval(key)] = raw_string_dict[key]
  return(RangeDict(new_dict))


# Retrieves the sheet that corresponds to the CR and type
def roller(challenge_rating, group_size):
  loot = {} 
  challenge_rating_range = challenge_rating_dict[challenge_rating]
  base_table_dict = item_db[group_size + challenge_rating_range]
  roll = random.randint(1,100)
  # Group Loot
  if group_size == "G":
    magic_item_list = magic_items(base_table_dict, roll)
    art_and_gem_list = art_and_gem(base_table_dict, roll)
    coins = []
    for coin in item_db['Group Gold']:
      number_of_coin = (str(dice_roller(item_db['Group Gold'][coin][challenge_rating_range])) + ' ' + coin)
      coins.append(number_of_coin)
    loot.update({"Magic Items": magic_item_list, "Art and Gems": art_and_gem_list, "Coins": coins})
  # Individual Loot
  else:
    coins = individual_currency(base_table_dict, roll)
    loot.update({"Coins": coins})
  return loot