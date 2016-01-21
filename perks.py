#!/usr/bin/env python

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
