#!/usr/bin/env python

class Perk():

    name = None
    rank = 0
    attribute = None
    attribute_rank = 0
    character_level = 0

    def __init__(self, name, attribute, attribute_rank, rank=1, character_level=0):
        self.name = name
        self.attribute = attribute
        self.attribute_rank = attribute_rank
        self.rank = rank
        self.character_level = character_level
