#!/usr/bin/env python

from perks import Perk
from attribute import Attribute

attribute_levels = {
            Attribute.STR:3,
            Attribute.PER:6,
            Attribute.END:3,
            Attribute.CHA:6,
            Attribute.INT:6,
            Attribute.AGI:4,
            Attribute.LCK:4
        }



# Current Perks
# Armourer - Rank 1
# Rifleman - Rank 2
# Awareness - Rank 1
# Locksmith - Rank 2
# Local Leader - Rank 1
# Gun Nut - Rank 2
# Hacker - Rank 2
# Scrapper - Rank 1
# Science! - Rank 1

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

