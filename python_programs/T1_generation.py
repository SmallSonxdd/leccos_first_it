import random
import string
from T1_tokens import *

def populate_T1_tokens(number_of_cultures, number_of_open_world):
    dict_of_tokens = {}
    cultures_and_open_worlds_chosen = random.sample(list_of_cultures, number_of_cultures) + random.sample(list_of_open_world, number_of_open_world)
    for culture_or_open_world in cultures_and_open_worlds_chosen:
        key, value = generate_T1_token(culture_or_open_world)
        dict_of_tokens[key] = value
    return (cultures_and_open_worlds_chosen, dict_of_tokens)


def generate_T1_token(culture_or_open_world):
    if culture_or_open_world not in list_of_cultures and culture_or_open_world not in list_of_open_world:
        raise Exception(f'Culture or open world {culture_or_open_world} not found')
    
    if culture_or_open_world in list_of_cultures:
        pos = dictionary_of_lists_cultures_to_positive_attributes[culture_or_open_world]
        neg = dictionary_of_lists_cultures_to_negative_attributes[culture_or_open_world]
        type = 'culture'
    else:
        pos = dictionary_of_lists_open_world_to_positive_attributes[culture_or_open_world]
        neg = dictionary_of_lists_open_world_to_negative_attributes[culture_or_open_world]
        type = 'open_world'

    pos_sd = random.uniform(1,2)
    num_pos = random.gauss(len(pos)/2, pos_sd)
    num_pos_rounded = round(num_pos)
    if num_pos_rounded > len(pos):
        num_pos_rounded = len(pos)
    elif num_pos_rounded < 0:
        num_pos_rounded = 0
    sample_pos = random.sample(pos, num_pos_rounded)

    neg_sd = random.uniform(1,2)    
    num_neg = random.gauss(len(neg)/2, neg_sd)
    num_neg_rounded = round(num_neg)
    if num_neg_rounded > len(neg):
        num_neg_rounded = len(neg)
    elif num_neg_rounded < 0:
        num_neg_rounded = 0
    sample_neg = random.sample(neg, num_neg_rounded)

    traits = sample_pos+sample_neg
    token_code = generate_token_code()

    key = culture_or_open_world 
    value = (traits, type, token_code, 'unused', f'Pos_number: {num_pos}. Pos_sd: {pos_sd}. Neg_number: {num_neg}. Neg_sd: {neg_sd}')
    
    """"
    print(f'pos sample is {sample_pos}')                    Just
    print('<>< <- this is a fish')                          Some
    print(f'neg sample is {sample_neg}')                    Animals
    print('V.v.V <- this is a crab')                        Out
    print(f'Full sample is {sample_pos+sample_neg}')        Here
    print('Final act, your doom!')                          !
    """
   
    return key, value

def generate_token_code():
    token_code = []
    alpha_list = list(string.ascii_letters)
    num_list = list(string.digits)
    count_alpha = round(random.gauss(4, 1)) 
    count_num = 8 - count_alpha
    for x in range(count_alpha):
        token_code.append(random.choice(alpha_list))
    for x in range(count_num):
        token_code.append(random.choice(num_list))
    random.shuffle(token_code)  
    return "".join(token_code)


#This is an alternative code that does discriminate against numbers for there are only 10 digits but 52 upper and lowercase letters
"""
def generate_token_code():
    token_code = []
    base_list = list(string.digits + string.ascii_letters)
    for x in range(8):
        token_code.append(random.choice(base_list))
    random.shuffle(token_code)
    return "".join(token_code)
"""
    

#Testing suite
"""
print('<<<<')
print(generate_T1_token('Piir-Bakka')) #prints generated dictionary of culture->(list of attributes, type, token code, status, random values)
print(generate_T1_token('Piir-Bakka')['Piir-Bakka'][0]) #prints generated dictionary entry's list of attributes, which is used as reference how to create T2 token
print(generate_T1_token('Piir-Bakka')['Piir-Bakka'][1]) #prints generated dictionary entry's type of token, which is used as reference for what type of T2 token is created
print(generate_T1_token('Piir-Bakka')['Piir-Bakka'][2]) #prints generated dictionary entry's token code, which is used as reference for T2 creation access
print(generate_T1_token('Piir-Bakka')['Piir-Bakka'][3]) #prints generated dictionary entry's status, which defaults to unused, which is used as reference for T2 creation availability
print(generate_T1_token('Piir-Bakka')['Piir-Bakka'][4]) #prints generated dictionary entry's string of random values that generated the list of attributes
print(generate_token_code()) #prints generated token code
print(populate_T1_tokens(4,4)) #prints list of 4 cultures and 4 open worlds to generate and generated dictionary
"""

