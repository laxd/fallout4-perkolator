#!/usr/bin/env python

from perks import Perk
from attribute import Attribute

def createRanks(name, attribute, attribute_rank, levels):
    perks = []

    for rank, level in enumerate(levels, start=1):
        perks.append(Perk(name, attribute, attribute_rank, rank, level))

    return perks

current_perks = []
desired_perks = ["Armorer", "Strong Back", "Pain Train", "Blacksmith",
        "Basher", "Locksmith", "Hacker"]

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

perks.extend(createRanks("Pickpocket", Attribute.PER, 1, [0,6,17,30]))
perks.extend(createRanks("Rifleman", Attribute.PER, 2, [0,9,18,31,46]))
perks.extend(createRanks("Awareness", Attribute.PER, 3, [0]))
perks.extend(createRanks("Locksmith", Attribute.PER, 4, [0,7,18,41]))
perks.extend(createRanks("Demolition Expert", Attribute.PER, 5, [0,10,22,34]))
perks.extend(createRanks("Night Person", Attribute.PER, 6, [0,25]))
perks.extend(createRanks("Refractor", Attribute.PER, 7, [0,11,21,35,42]))
perks.extend(createRanks("Sniper", Attribute.PER, 8, [0,13,26]))
perks.extend(createRanks("Penetrator", Attribute.PER, 9, [0,28]))
perks.extend(createRanks("Concentrated Fire", Attribute.PER, 10, [0,26,50]))

perks.extend(createRanks("Toughness", Attribute.END, 1, [0,9,18,31,46]))
perks.extend(createRanks("Lead Belly", Attribute.END, 2, [0,6,17]))
perks.extend(createRanks("Lifegiver", Attribute.END, 3, [0,8,20]))
perks.extend(createRanks("Chem Resistant", Attribute.END, 4, [0,22]))
perks.extend(createRanks("Aquaboy/Aquagirl", Attribute.END, 5, [0,21]))
perks.extend(createRanks("Rad Resistant", Attribute.END, 6, [0,13,26]))
perks.extend(createRanks("Adamantium Skeleton", Attribute.END, 7, [0,13,26]))
perks.extend(createRanks("Cannibal", Attribute.END, 8, [0,19,38]))
perks.extend(createRanks("Ghoulish", Attribute.END, 9, [0,24,48]))
perks.extend(createRanks("Solar Powered", Attribute.END, 10, [0,27,50]))

perks.extend(createRanks("Cap Collector", Attribute.CHA, 1, [0,20,41]))
perks.extend(createRanks("Lady Killer/Black Widow", Attribute.CHA, 2, [0,7,16]))
perks.extend(createRanks("Lone Wonderer", Attribute.CHA, 3, [0,17,40]))
perks.extend(createRanks("Attack Dog", Attribute.CHA, 4, [0,9,25]))
perks.extend(createRanks("Animal Friend", Attribute.CHA, 5, [0,12,28]))
perks.extend(createRanks("Local Leader", Attribute.CHA, 6, [0,14]))
perks.extend(createRanks("Party Boy/Party Girl", Attribute.CHA, 7, [0,15,37]))
perks.extend(createRanks("Inspirational", Attribute.CHA, 8, [0,19,43]))
perks.extend(createRanks("Wasteland Whisperer", Attribute.CHA, 9, [0,21,49]))
perks.extend(createRanks("Intimidation", Attribute.CHA, 10, [0,23,50]))

perks.extend(createRanks("V.A.N.S", Attribute.INT, 1, [0]))
perks.extend(createRanks("Medic", Attribute.INT, 2, [0,18,30,49]))
perks.extend(createRanks("Gun Nut", Attribute.INT, 3, [0,13,25,39]))
perks.extend(createRanks("Hacker", Attribute.INT, 4, [0,9,21,33]))
perks.extend(createRanks("Scrapper", Attribute.INT, 5, [0,23]))
perks.extend(createRanks("Science!", Attribute.INT, 6, [0,17,28,41]))
perks.extend(createRanks("Chemist", Attribute.INT, 7, [0,16,32,45]))
perks.extend(createRanks("Robotics Expert", Attribute.INT, 8, [0,19,44]))
perks.extend(createRanks("Nuclear Physicist", Attribute.INT, 9, [0,14,26]))
perks.extend(createRanks("Nerd Rage!", Attribute.INT, 10, [0,31,50]))

perks.extend(createRanks("Gunslinger", Attribute.AGI, 1, [0,7,15,27,42]))
perks.extend(createRanks("Commando", Attribute.AGI, 2, [0,11,21,35,49]))
perks.extend(createRanks("Sneak", Attribute.AGI, 3, [0,5,12,23,38]))
perks.extend(createRanks("Mister Sandman", Attribute.AGI, 4, [0,17,30]))
perks.extend(createRanks("Action Boy/Action Girl", Attribute.AGI, 5, [0,18]))
perks.extend(createRanks("Moving Target", Attribute.AGI, 6, [0,24,44]))
perks.extend(createRanks("Ninja", Attribute.AGI, 7, [0,16,33]))
perks.extend(createRanks("Quick Hands", Attribute.AGI, 8, [0,28]))
perks.extend(createRanks("Blitz", Attribute.AGI, 9, [0,29]))
perks.extend(createRanks("Gun Fu", Attribute.AGI, 10, [0,26,50]))

perks.extend(createRanks("Fortune Finder", Attribute.LCK, 1, [0,5,25,40]))
perks.extend(createRanks("Scrounger", Attribute.LCK, 2, [0,7,24,37]))
perks.extend(createRanks("Bloody Mess", Attribute.LCK, 3, [0,9,31,47]))
perks.extend(createRanks("Mysterious Stranger", Attribute.LCK, 4, [0,22,41]))
perks.extend(createRanks("Idiot Savant", Attribute.LCK, 5, [0,11,34]))
perks.extend(createRanks("Better Criticals", Attribute.LCK, 6, [0,15,40]))
perks.extend(createRanks("Critical Banker", Attribute.LCK, 7, [0,17,43]))
perks.extend(createRanks("Grim Reaper's Sprint", Attribute.LCK, 8, [0,19,46]))
perks.extend(createRanks("Four Leaf Clover", Attribute.LCK, 9, [0,13,32,48]))
perks.extend(createRanks("Ricochet", Attribute.LCK, 10, [0,29,50]))

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

