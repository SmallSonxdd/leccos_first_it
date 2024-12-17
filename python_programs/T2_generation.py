import random
from T1_generation import generate_token_code

def generate_T2_token(tokens_database, token_one_name_in_database, token_two_name_in_database, tarot):
    token_1 = tokens_database[1][token_one_name_in_database]
    token_2 = tokens_database[1][token_two_name_in_database]
    token_1[3] = 'Depleted'
    token_2[3] = 'Depleted'
    new_token_name = token_one_name_in_database + '+' + token_two_name_in_database + '+' + tarot.tarot_name
    tokens_attributes = token_1[0] + token_2[0]
    remainder_sd = random.uniform(0,1)
    remainder_num = random.gauss(len(tokens_attributes)/1.25, remainder_sd)
    rounded_num = round(remainder_num)
    if rounded_num > len(tokens_attributes):
        rounded_num = len(tokens_attributes)
    elif rounded_num < 0:
        rounded_num = 0
    remainder_sample = random.sample(tokens_attributes, rounded_num)
    tarot_sd = random.uniform(1,2)
    tarot_num = random.gauss(len(tarot.attributes)/4, tarot_sd)
    tarot_rounded = round(tarot_num)
    if tarot_rounded > len(tarot.attributes):
        tarot_rounded = len(tarot.attributes)
    elif tarot_rounded < 0:
        tarot_rounded = 0
    tarot_sample = random.sample(tarot.attributes, tarot_rounded)
    new_token_attributes = remainder_sample + tarot_sample
    #time to generate type
    if token_1[1] == 'culture' and token_1[1] == token_2[1]:
        new_token_type = 'majestyx'
    elif token_1[1] == 'open_world' and token_1[1] == token_2[1]:
        new_token_type = 'journey'
    elif (token_1[1] == 'open_world' and token_2[1] == 'culture') or (token_1[1] == 'culture' and token_2[1] == 'open_world'):
        new_token_type = 'character'
    else:
        raise Exception("I've been given invalid token types to merge, beep boop I'm a bot (neverlucky)")
    new_token_code = generate_token_code()

    return (new_token_name, new_token_attributes, new_token_type, new_token_code, 'Activate', f'Pos_number: {remainder_num}. Pos_sd: {remainder_sd}. Neg_number: {tarot_num}. Neg_sd: {tarot_sd}')