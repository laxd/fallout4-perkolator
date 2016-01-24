#!/usr/bin/env python

from attribute import Attribute

class Perk():

    def __init__(self, name, attribute, attribute_rank, rank=1, character_level=0):
        self.name = name
        self.attribute = attribute
        self.attribute_rank = attribute_rank
        self.rank = rank
        self.character_level = character_level

    def __str__(self):
        return "{name} - Rank {rank} - Requires {attr} at {attr_level}".format(name=self.name, rank=self.rank, attr=self.attribute, attr_level=self.attribute_rank)

    def __eq__(self, other):
        if not isinstance(other, Perk):
            return False

        return (self.name == other.name
            and self.attribute == other.attribute
            and self.rank == other.rank)

def create_ranks(name, attribute, attribute_rank, levels):
    perks = []

    for rank, level in enumerate(levels, start=1):
        perk = Perk(name, attribute, attribute_rank, rank, level)
        perks.append(perk)

    return perks

def get_all_perks():
    perks = []

    perks.extend(create_ranks("Iron Fist", Attribute.STR, 1, [0,9,18,31,46]))
    perks.extend(create_ranks("Big Leagues", Attribute.STR, 2, [0,7,15,27,42]))
    perks.extend(create_ranks("Armorer", Attribute.STR, 3, [0,13,25,39]))
    perks.extend(create_ranks("Blacksmith", Attribute.STR, 4, [0,16,29]))
    perks.extend(create_ranks("Heavy Gunner", Attribute.STR, 5, [0,11,21,35,47]))
    perks.extend(create_ranks("Strong Back", Attribute.STR, 6, [0,10,20,30]))
    perks.extend(create_ranks("Steady Aim", Attribute.STR, 7, [0,28]))
    perks.extend(create_ranks("Basher", Attribute.STR, 8, [0,5,14,26]))
    perks.extend(create_ranks("Rooted", Attribute.STR, 9, [0,22,43]))
    perks.extend(create_ranks("Pain Train", Attribute.STR, 10, [0,24,50]))

    perks.extend(create_ranks("Pickpocket", Attribute.PER, 1, [0,6,17,30]))
    perks.extend(create_ranks("Rifleman", Attribute.PER, 2, [0,9,18,31,46]))
    perks.extend(create_ranks("Awareness", Attribute.PER, 3, [0]))
    perks.extend(create_ranks("Locksmith", Attribute.PER, 4, [0,7,18,41]))
    perks.extend(create_ranks("Demolition Expert", Attribute.PER, 5, [0,10,22,34]))
    perks.extend(create_ranks("Night Person", Attribute.PER, 6, [0,25]))
    perks.extend(create_ranks("Refractor", Attribute.PER, 7, [0,11,21,35,42]))
    perks.extend(create_ranks("Sniper", Attribute.PER, 8, [0,13,26]))
    perks.extend(create_ranks("Penetrator", Attribute.PER, 9, [0,28]))
    perks.extend(create_ranks("Concentrated Fire", Attribute.PER, 10, [0,26,50]))

    perks.extend(create_ranks("Toughness", Attribute.END, 1, [0,9,18,31,46]))
    perks.extend(create_ranks("Lead Belly", Attribute.END, 2, [0,6,17]))
    perks.extend(create_ranks("Lifegiver", Attribute.END, 3, [0,8,20]))
    perks.extend(create_ranks("Chem Resistant", Attribute.END, 4, [0,22]))
    perks.extend(create_ranks("Aquaboy/Aquagirl", Attribute.END, 5, [0,21]))
    perks.extend(create_ranks("Rad Resistant", Attribute.END, 6, [0,13,26]))
    perks.extend(create_ranks("Adamantium Skeleton", Attribute.END, 7, [0,13,26]))
    perks.extend(create_ranks("Cannibal", Attribute.END, 8, [0,19,38]))
    perks.extend(create_ranks("Ghoulish", Attribute.END, 9, [0,24,48]))
    perks.extend(create_ranks("Solar Powered", Attribute.END, 10, [0,27,50]))

    perks.extend(create_ranks("Cap Collector", Attribute.CHA, 1, [0,20,41]))
    perks.extend(create_ranks("Lady Killer/Black Widow", Attribute.CHA, 2, [0,7,16]))
    perks.extend(create_ranks("Lone Wonderer", Attribute.CHA, 3, [0,17,40]))
    perks.extend(create_ranks("Attack Dog", Attribute.CHA, 4, [0,9,25]))
    perks.extend(create_ranks("Animal Friend", Attribute.CHA, 5, [0,12,28]))
    perks.extend(create_ranks("Local Leader", Attribute.CHA, 6, [0,14]))
    perks.extend(create_ranks("Party Boy/Party Girl", Attribute.CHA, 7, [0,15,37]))
    perks.extend(create_ranks("Inspirational", Attribute.CHA, 8, [0,19,43]))
    perks.extend(create_ranks("Wasteland Whisperer", Attribute.CHA, 9, [0,21,49]))
    perks.extend(create_ranks("Intimidation", Attribute.CHA, 10, [0,23,50]))

    perks.extend(create_ranks("V.A.N.S", Attribute.INT, 1, [0]))
    perks.extend(create_ranks("Medic", Attribute.INT, 2, [0,18,30,49]))
    perks.extend(create_ranks("Gun Nut", Attribute.INT, 3, [0,13,25,39]))
    perks.extend(create_ranks("Hacker", Attribute.INT, 4, [0,9,21,33]))
    perks.extend(create_ranks("Scrapper", Attribute.INT, 5, [0,23]))
    perks.extend(create_ranks("Science!", Attribute.INT, 6, [0,17,28,41]))
    perks.extend(create_ranks("Chemist", Attribute.INT, 7, [0,16,32,45]))
    perks.extend(create_ranks("Robotics Expert", Attribute.INT, 8, [0,19,44]))
    perks.extend(create_ranks("Nuclear Physicist", Attribute.INT, 9, [0,14,26]))
    perks.extend(create_ranks("Nerd Rage!", Attribute.INT, 10, [0,31,50]))

    perks.extend(create_ranks("Gunslinger", Attribute.AGI, 1, [0,7,15,27,42]))
    perks.extend(create_ranks("Commando", Attribute.AGI, 2, [0,11,21,35,49]))
    perks.extend(create_ranks("Sneak", Attribute.AGI, 3, [0,5,12,23,38]))
    perks.extend(create_ranks("Mister Sandman", Attribute.AGI, 4, [0,17,30]))
    perks.extend(create_ranks("Action Boy/Action Girl", Attribute.AGI, 5, [0,18]))
    perks.extend(create_ranks("Moving Target", Attribute.AGI, 6, [0,24,44]))
    perks.extend(create_ranks("Ninja", Attribute.AGI, 7, [0,16,33]))
    perks.extend(create_ranks("Quick Hands", Attribute.AGI, 8, [0,28]))
    perks.extend(create_ranks("Blitz", Attribute.AGI, 9, [0,29]))
    perks.extend(create_ranks("Gun Fu", Attribute.AGI, 10, [0,26,50]))

    perks.extend(create_ranks("Fortune Finder", Attribute.LCK, 1, [0,5,25,40]))
    perks.extend(create_ranks("Scrounger", Attribute.LCK, 2, [0,7,24,37]))
    perks.extend(create_ranks("Bloody Mess", Attribute.LCK, 3, [0,9,31,47]))
    perks.extend(create_ranks("Mysterious Stranger", Attribute.LCK, 4, [0,22,41]))
    perks.extend(create_ranks("Idiot Savant", Attribute.LCK, 5, [0,11,34]))
    perks.extend(create_ranks("Better Criticals", Attribute.LCK, 6, [0,15,40]))
    perks.extend(create_ranks("Critical Banker", Attribute.LCK, 7, [0,17,43]))
    perks.extend(create_ranks("Grim Reaper's Sprint", Attribute.LCK, 8, [0,19,46]))
    perks.extend(create_ranks("Four Leaf Clover", Attribute.LCK, 9, [0,13,32,48]))
    perks.extend(create_ranks("Ricochet", Attribute.LCK, 10, [0,29,50]))

    return perks
