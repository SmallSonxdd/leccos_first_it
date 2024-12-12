import random
import string
from T1_tokens import *

def generate_T1_token(culture_or_open_world):
    if culture_or_open_world not in list_of_cultures and culture_or_open_world not in list_of_open_world:
        raise Exception(f'Culture or open world {culture_or_open_world} not found')
    
    if culture_or_open_world in list_of_cultures:
        pos = dictionary_of_lists_cultures_to_positive_attributes[culture_or_open_world]
        neg = dictionary_of_lists_cultures_to_negative_attributes[culture_or_open_world]
    else:
        pos = dictionary_of_lists_open_world_to_positive_attributes[culture_or_open_world]
        neg = dictionary_of_lists_open_world_to_negative_attributes[culture_or_open_world]
    
    pos_sd = random.uniform(1,2)
    num_pos = random.gauss(len(pos)/2, pos_sd)
    num_pos_rounded = round(num_pos)
    sample_pos = random.sample(pos, num_pos_rounded)

    neg_sd = random.uniform(1,2)    
    num_neg = random.gauss(len(neg)/2, neg_sd)
    num_neg_rounded = round(num_neg)
    sample_neg = random.sample(neg, num_neg_rounded)

    traits = sample_pos+sample_neg
    token_code = generate_token_code()

    dict = {culture_or_open_world: (traits, token_code, f'Pos_number: {num_pos}. Pos_sd: {pos_sd}. Neg_number: {num_neg}. Neg_sd: {neg_sd}')}
    
    """"
    print(f'pos sample is {sample_pos}')                    Just
    print('<>< <- this is a fish')                          Some
    print(f'neg sample is {sample_neg}')                    Animals
    print('V.v.V <- this is a crab')                        Out
    print(f'Full sample is {sample_pos+sample_neg}')        Here
    print('Final act, your doom!')                          !
    """
   
    return dict

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
print(generate_T1_token('Piir-Bakka')) #prints generated dictionary of culture->(list of attributes, token code, random values)
print(generate_T1_token('Piir-Bakka')['Piir-Bakka'][0]) #prints generated dictionary's list of attributes
print(generate_T1_token('Piir-Bakka')['Piir-Bakka'][1]) #prints generated dictionary's token code
print(generate_T1_token('Piir-Bakka')['Piir-Bakka'][2]) #prints generated dictionary's string of random values that generated the list of attributes
print(generate_token_code())
"""

