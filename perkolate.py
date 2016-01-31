#!/usr/bin/env python

from perks import Perk
from attribute import Attribute

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

