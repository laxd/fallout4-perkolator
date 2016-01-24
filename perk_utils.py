from attribute import Attribute
from perks import Perk, Rank


def create_ranks(name, attribute, attribute_level, levels):
    ranks = []

    for rank, level in enumerate(levels, start=1):
        ranks.append(Rank(rank, level, ""))

    return Perk(name, attribute, attribute_level, ranks)

perks = {}

STR_perks = []
STR_perks.append(create_ranks("Iron Fist", Attribute.STR, 1, [0,9,18,31,46]))
STR_perks.append(create_ranks("Big Leagues", Attribute.STR, 2, [0,7,15,27,42]))
STR_perks.append(create_ranks("Armorer", Attribute.STR, 3, [0,13,25,39]))
STR_perks.append(create_ranks("Blacksmith", Attribute.STR, 4, [0,16,29]))
STR_perks.append(create_ranks("Heavy Gunner", Attribute.STR, 5, [0,11,21,35,47]))
STR_perks.append(create_ranks("Strong Back", Attribute.STR, 6, [0,10,20,30]))
STR_perks.append(create_ranks("Steady Aim", Attribute.STR, 7, [0,28]))
STR_perks.append(create_ranks("Basher", Attribute.STR, 8, [0,5,14,26]))
STR_perks.append(create_ranks("Rooted", Attribute.STR, 9, [0,22,43]))
STR_perks.append(create_ranks("Pain Train", Attribute.STR, 10, [0,24,50]))
perks[Attribute.STR] = STR_perks

PER_perks = []
PER_perks.append(create_ranks("Pickpocket", Attribute.PER, 1, [0,6,17,30]))
PER_perks.append(create_ranks("Rifleman", Attribute.PER, 2, [0,9,18,31,46]))
PER_perks.append(create_ranks("Awareness", Attribute.PER, 3, [0]))
PER_perks.append(create_ranks("Locksmith", Attribute.PER, 4, [0,7,18,41]))
PER_perks.append(create_ranks("Demolition Expert", Attribute.PER, 5, [0,10,22,34]))
PER_perks.append(create_ranks("Night Person", Attribute.PER, 6, [0,25]))
PER_perks.append(create_ranks("Refractor", Attribute.PER, 7, [0,11,21,35,42]))
PER_perks.append(create_ranks("Sniper", Attribute.PER, 8, [0,13,26]))
PER_perks.append(create_ranks("Penetrator", Attribute.PER, 9, [0,28]))
PER_perks.append(create_ranks("Concentrated Fire", Attribute.PER, 10, [0,26,50]))
perks[Attribute.PER] = PER_perks

END_perks = []
END_perks.append(create_ranks("Toughness", Attribute.END, 1, [0,9,18,31,46]))
END_perks.append(create_ranks("Lead Belly", Attribute.END, 2, [0,6,17]))
END_perks.append(create_ranks("Lifegiver", Attribute.END, 3, [0,8,20]))
END_perks.append(create_ranks("Chem Resistant", Attribute.END, 4, [0,22]))
END_perks.append(create_ranks("Aquaboy/Aquagirl", Attribute.END, 5, [0,21]))
END_perks.append(create_ranks("Rad Resistant", Attribute.END, 6, [0,13,26]))
END_perks.append(create_ranks("Adamantium Skeleton", Attribute.END, 7, [0,13,26]))
END_perks.append(create_ranks("Cannibal", Attribute.END, 8, [0,19,38]))
END_perks.append(create_ranks("Ghoulish", Attribute.END, 9, [0,24,48]))
END_perks.append(create_ranks("Solar Powered", Attribute.END, 10, [0,27,50]))
perks[Attribute.END] = END_perks

CHA_perks = []
CHA_perks.append(create_ranks("Cap Collector", Attribute.CHA, 1, [0,20,41]))
CHA_perks.append(create_ranks("Lady Killer/Black Widow", Attribute.CHA, 2, [0,7,16]))
CHA_perks.append(create_ranks("Lone Wonderer", Attribute.CHA, 3, [0,17,40]))
CHA_perks.append(create_ranks("Attack Dog", Attribute.CHA, 4, [0,9,25]))
CHA_perks.append(create_ranks("Animal Friend", Attribute.CHA, 5, [0,12,28]))
CHA_perks.append(create_ranks("Local Leader", Attribute.CHA, 6, [0,14]))
CHA_perks.append(create_ranks("Party Boy/Party Girl", Attribute.CHA, 7, [0,15,37]))
CHA_perks.append(create_ranks("Inspirational", Attribute.CHA, 8, [0,19,43]))
CHA_perks.append(create_ranks("Wasteland Whisperer", Attribute.CHA, 9, [0,21,49]))
CHA_perks.append(create_ranks("Intimidation", Attribute.CHA, 10, [0,23,50]))
perks[Attribute.CHA] = CHA_perks

INT_perks = []
INT_perks.append(create_ranks("V.A.N.S", Attribute.INT, 1, [0]))
INT_perks.append(create_ranks("Medic", Attribute.INT, 2, [0,18,30,49]))
INT_perks.append(create_ranks("Gun Nut", Attribute.INT, 3, [0,13,25,39]))
INT_perks.append(create_ranks("Hacker", Attribute.INT, 4, [0,9,21,33]))
INT_perks.append(create_ranks("Scrapper", Attribute.INT, 5, [0,23]))
INT_perks.append(create_ranks("Science!", Attribute.INT, 6, [0,17,28,41]))
INT_perks.append(create_ranks("Chemist", Attribute.INT, 7, [0,16,32,45]))
INT_perks.append(create_ranks("Robotics Expert", Attribute.INT, 8, [0,19,44]))
INT_perks.append(create_ranks("Nuclear Physicist", Attribute.INT, 9, [0,14,26]))
INT_perks.append(create_ranks("Nerd Rage!", Attribute.INT, 10, [0,31,50]))
perks[Attribute.INT] = INT_perks

AGI_perks = []
AGI_perks.append(create_ranks("Gunslinger", Attribute.AGI, 1, [0,7,15,27,42]))
AGI_perks.append(create_ranks("Commando", Attribute.AGI, 2, [0,11,21,35,49]))
AGI_perks.append(create_ranks("Sneak", Attribute.AGI, 3, [0,5,12,23,38]))
AGI_perks.append(create_ranks("Mister Sandman", Attribute.AGI, 4, [0,17,30]))
AGI_perks.append(create_ranks("Action Boy/Action Girl", Attribute.AGI, 5, [0,18]))
AGI_perks.append(create_ranks("Moving Target", Attribute.AGI, 6, [0,24,44]))
AGI_perks.append(create_ranks("Ninja", Attribute.AGI, 7, [0,16,33]))
AGI_perks.append(create_ranks("Quick Hands", Attribute.AGI, 8, [0,28]))
AGI_perks.append(create_ranks("Blitz", Attribute.AGI, 9, [0,29]))
AGI_perks.append(create_ranks("Gun Fu", Attribute.AGI, 10, [0,26,50]))
perks[Attribute.AGI] = AGI_perks

LCK_perks = []
LCK_perks.append(create_ranks("Fortune Finder", Attribute.LCK, 1, [0,5,25,40]))
LCK_perks.append(create_ranks("Scrounger", Attribute.LCK, 2, [0,7,24,37]))
LCK_perks.append(create_ranks("Bloody Mess", Attribute.LCK, 3, [0,9,31,47]))
LCK_perks.append(create_ranks("Mysterious Stranger", Attribute.LCK, 4, [0,22,41]))
LCK_perks.append(create_ranks("Idiot Savant", Attribute.LCK, 5, [0,11,34]))
LCK_perks.append(create_ranks("Better Criticals", Attribute.LCK, 6, [0,15,40]))
LCK_perks.append(create_ranks("Critical Banker", Attribute.LCK, 7, [0,17,43]))
LCK_perks.append(create_ranks("Grim Reaper's Sprint", Attribute.LCK, 8, [0,19,46]))
LCK_perks.append(create_ranks("Four Leaf Clover", Attribute.LCK, 9, [0,13,32,48]))
LCK_perks.append(create_ranks("Ricochet", Attribute.LCK, 10, [0,29,50]))
perks[Attribute.LCK] = LCK_perks
