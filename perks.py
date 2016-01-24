#!/usr/bin/env python

from attribute import Attribute

class Perk():

    def __init__(self, name, attribute, attribute_level, ranks):
        self.name = name
        self.attribute = attribute
        self.attribute_level = attribute_level
        self.ranks = ranks

    def __str__(self):
        return "{name} - {attr} at {attr_level}".format(name=self.name, attr=self.attribute, attr_level=self.attribute_level)

    def __eq__(self, other):
        if not isinstance(other, Perk):
            return False

        return (self.name == other.name
            and self.attribute == other.attribute
            and self.attribute_level == other.attribute_level)

class Rank():
    def __init__(self, rank_level, required_level, description):
        self.rank_level = rank_level
        self.required_level = required_level
        self.description = description
