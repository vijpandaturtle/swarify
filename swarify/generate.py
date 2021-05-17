import math
import random
import numpy as np
from itertools import permutations

def main_pattern(num_notes, num_bars):
    '''Generate the main pattern'''
    pattern_nos = list(range(num_notes))
    p = permutations(pattern_nos)
    perm = list(p)
    pattern = random.sample(perm,num_bars)
    pattern = np.array(pattern)
    pattern = pattern.flatten()
    return pattern

def generate_pattern(main_pattern, notes, ending):
    '''Generate the alankar from the main pattern'''
    gen_pattern = []
    for i in range(len(notes)):
        next_pat = []
        for index in main_pattern:
            note = notes[index+i]
            next_pat.append(note)
        gen_pattern.append(next_pat)
        if next_pat[-1] == ending:
            #gen_pattern.append("----------------")
            break
    return gen_pattern

def alankar_generator(num_notes, num_bars):
    '''Combining the main pattern and generation functions'''
    notes_asc = ['S', 'R', 'G', 'M', 'P', 'D', 'N', 'Ṡ', 'Ṙ', 'Ġ', 'Ṁ', 'Ṗ']
    notes_desc = ['Ṡ','N', 'D', 'P', 'M', 'G', 'R', 'S', 'Ṇ', 'Ḍ', 'P̣']
    if num_bars > math.factorial(num_notes):
        return "Too  many  bars"
    pattern = main_pattern(num_notes, num_bars)
    full_pattern = generate_pattern(pattern, notes_asc, 'Ṡ')
    full_pattern_desc = generate_pattern(pattern, notes_desc, 'S')
    return (full_pattern + full_pattern_desc)
