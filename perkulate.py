#!/usr/bin/env python

from perks import Perk
from attribute import Attribute

def createRanks(name, attribute, attribute_rank, levels):
    perks = []

    for rank, level in enumerate(levels, start=1):
        perks.append(Perk(name, attribute, attribute_rank, rank, level))

    return perks

current_perks = []
desired_perks = ["Armorer", "Strong Back", "Pain Train"]

perks = []

perks.extend(createRanks("Iron Fist", Attribute.STR, 1, [0,9,18,31,46]))
perks.extend(createRanks("Big Leagues", Attribute.STR, 2, [0,7,15,27,42]))
perks.extend(createRanks("Armorer", Attribute.STR, 3, [0,13,25,39]))
perks.extend(createRanks("Blacksmith", Attribute.STR, 4, [0,16,29]))
perks.extend(createRanks("Heavy Gunner", Attribute.STR, 5, [0,11,21,35,47]))
perks.extend(createRanks("Strong Back", Attribute.STR, 6, [0,10,20,30]))
perks.extend(createRanks("Steady Aim", Attribute.STR, 7, [0,28]))
perks.extend(createRanks("Basher", Attribute.STR, 8, [0,5,14,26]))
perks.extend(createRanks("Rooted", Attribute.STR, 9, [0,22,43]))
perks.extend(createRanks("Pain Train", Attribute.STR, 10, [0,24,50]))

for level in range(1,50):
    perk_found = False
    for perk in perks:
        if perk.name in desired_perks and level > perk.character_level and perk not in current_perks:
            perk_found = True
            print("Recommended for level {level}: {name} - Rank {rank}".format(name=perk.name, rank=perk.rank, level=level))
            current_perks.append(perk)
            break
    
    if not perk_found:
        print("Recommended for level {level}: Nothing!".format(level=level))

