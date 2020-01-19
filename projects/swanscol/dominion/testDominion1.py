# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 10:08 2020

@author: Cole Swanson
"""

import Dominion
import random
from collections import defaultdict
import testUtility

#Get player names
player_names = ["Annie"]

#number of curses and victory cards
nV = testUtility.GetVictNum(player_names)
nC = -10 + 10 * len(player_names)

#Define box
box = testUtility.GetBoxes(nV)

supply_order = testUtility.GetSupplyOrder()

supply = testUtility.GetSupply(box, nV, nC, player_names)
supply["Copper"] = [Dominion.Copper()] * (60 - len(player_names) * 7)
supply["Silver"] = [Dominion.Copper()] * 40
supply["Gold"] = [Dominion.Copper()] * 30

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.GetPlayers(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)