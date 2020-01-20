# -*- coding: utf-8 -*-
"""
Created on Thursday Jan 16 2020

@author: Elliott Lapinel
"""

import Dominion
import random
from collections import defaultdict
import testUtility

# Get player names
player_names = ["Annie", "*Ben", "*Carla"]

# number of curses and victory cards
if len(player_names) > 2:
    nV = 12
else:
    nV = 8
nC = -10 + 10 * len(player_names)

# create the cards
box = testUtility.getBoxes(nV)
# create the supply
supply_order = testUtility.getSupply()



# Pick 10 cards from box to be in the supply.
supply = testUtility.boxToSupply(box)


# The supply always has these cards
#incorrectly reverse proper order of nC and nV
testUtility.initializeSupply(player_names, nV, nC, supply)


# initialize the trash
trash = []

# Construct the Player objects
players = testUtility.playerSetup(player_names)


# Play the game
testUtility.playGame(trash, supply, supply_order, players)



# Final score
testUtility.checkScore()

