import random
from T1_tokens import *
from major_arcana_tarots import *

list_of_all_tarots = list_of_cultures + list_of_open_world + list_of_major_arcana

def populate_tarots(number_of_tarots):
    list_of_tarot_cards = []
    for index in range(number_of_tarots):
        tarot = generate_tarot()
        while (tarot in list_of_tarot_cards):
            tarot = generate_tarot()
        list_of_tarot_cards.append(tarot)
    return list_of_tarot_cards

def generate_tarot():
    position = random.randint(0, 1)
    tarot = (random.sample(list_of_all_tarots, 1))[0]
    tarot_attributes = None
    if tarot in list_of_cultures:
        if position == 0:
            tarot_attributes = dictionary_of_lists_cultures_to_positive_attributes[tarot]
        elif position == 1:
            tarot_attributes = dictionary_of_lists_cultures_to_negative_attributes[tarot]        
    elif tarot in list_of_open_world:
        if position == 0:
            tarot_attributes = dictionary_of_lists_open_world_to_positive_attributes[tarot]
        elif position == 1:
            tarot_attributes = dictionary_of_lists_open_world_to_negative_attributes[tarot]  
    elif tarot in list_of_major_arcana:
        if position == 0:
            tarot_attributes = dictionary_of_lists_major_arcana_to_positive_attributes[tarot]
        elif position == 1:
            tarot_attributes = dictionary_of_lists_major_arcana_to_negative_attributes[tarot]  
    else:
        raise Exception('Invalid tarot type')
    return (tarot, position, tarot_attributes)

#Testing suite
"""
print(populate_tarots(3))
"""