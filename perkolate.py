#!/usr/bin/env python

from perks import Perk
from attribute import Attribute

perks = []

def get_perks(perk_names_and_rank, perks):
    perks = []

    for index, name_rank in enumerate(perk_names_and_rank):
        if isinstance(name_rank, tuple):
            print("Checking for {0}".format(name_rank))
            if name_rank in perks:
                perks.append(perks[name_rank])
        else:
            i = 1;
            print("Checking if {perk} is available: {status}".format(perk=name_rank, status=((name_rank, i) in perks)))
            while (name_rank, i) in perks:
                perks.append(perks[(name_rank, i)])
                i += 1

    return perks

attribute_levels = {
            Attribute.STR:3,
            Attribute.PER:3,
            Attribute.END:3,
            Attribute.CHA:3,
            Attribute.INT:3,
            Attribute.AGI:3,
            Attribute.LCK:3
        }



current_perks = []
desired_perks = create_ranks("Ninja", Attribute.AGI, 7, [0,16,33])

for level in range(1,50):
    print("Level {level}".format(level=level))
    perk_found = False
    for perk in perks:
        if (perk in desired_perks 
        and level > perk.character_level
        and perk not in current_perks
        and perk.attribute_rank >= attribute_levels[perk.attribute]):
            perk_found = True
            print("Recommended for level {level}: {name} - Rank {rank}".format(name=perk.name, rank=perk.rank, level=level))
            current_perks.append(perk)
            break


    
    if not perk_found:
        for perk in desired_perks:
            if perk not in current_perks and perk.attribute_rank > attribute_levels[perk.attribute]:
                attribute_levels[perk.attribute] = attribute_levels[perk.attribute] + 1
                print("Recommended for level {level}: Increase Attribute {attr} to {attr_level}".format(level=level, attr=perk.attribute, attr_level=attribute_levels[perk.attribute]))
                break

