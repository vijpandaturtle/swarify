import random
import numpy as np
from itertools import permutations

def main_pattern(num_notes, num_bars):
    pattern_nos = list(range(num_notes))
    p = permutations(pattern_nos)
    perm = list(p)
    pattern = random.sample(perm,num_bars)
    pattern = np.array(pattern)
    pattern = pattern.flatten()
    return pattern

def generate_pattern(main_pattern, notes):
    gen_pattern = []
    for i in range(len(notes)):
        next_pat = []
        for index in pattern:
            note = notes[index+i]
            next_pat.append(note)
        gen_pattern.append(next_pat)
        if next_pat[-1] == 'S'or next_pat[-1] == 'Ṡ':
            break
    return gen_pattern

def display_pattern(pattern):
    for pat in pattern:
        print(pat)


if __name__ == "__main__":

    num_notes = 7
    num_bars = 4
    notes = ['S', 'R', 'G', 'M', 'P', 'D', 'N', 'Ṡ']
    total_notes = ['P̣', 'Ḍ', 'Ṇ', 'S', 'R', 'G', 'M', 'P', 'D', 'N', 'Ṡ', 'Ṙ', 'Ġ', 'Ṁ', 'Ṗ']
    notes_asc = notes.copy()
    notes_desc = notes.copy()[::-1]
    notes_long_asc = ['S', 'R', 'G', 'M', 'P', 'D', 'N', 'Ṡ', 'Ṙ', 'Ġ', 'Ṁ', 'Ṗ']
    notes_long_desc = ['Ṡ','N', 'D', 'P', 'M', 'G', 'R', 'S', 'Ṇ', 'Ḍ', 'P̣']

    pattern = main_pattern(num_notes, num_bars)
    #notes = ['P̣', 'Ḍ', 'Ṇ', 'S', 'R', 'G', 'M', 'P', 'D', 'N', 'Ṡ', 'Ṙ', 'Ġ', 'Ṁ', 'Ṗ']
    # full_pattern = generate_pattern(pattern, notes_asc)
    # full_pattern_desc = generate_pattern(pattern, notes_desc)

    # full_pattern = generate_pattern(pattern, notes_long_asc)
    # full_pattern_desc = generate_pattern(pattern, notes_long_desc)

    display_pattern(full_pattern)
    print("-------------------------------")
    display_pattern(full_pattern_desc)


