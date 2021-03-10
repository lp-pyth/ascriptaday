# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 18:02:55 2021
rock, paper, scissors
@author: lux
"""
import random
import time
import sys

sleeptime = 0.4
quitgame = False
okhands = ['Rock', 'Paper', 'Scissors']

def quitnow():
    wannaquit = input('Do you want to play another game? (y/n): ')
    if wannaquit == 'n':
        print('')
        print('Thank you for playing!')
        sys.exit()
    elif wannaquit == 'y':
        print('')
        print('Ok, another time!')
    else:
        print('')
        print('You did not type correctly.')
        time.sleep(sleeptime)
        quitnow()       
        
def playgame():
    while quitgame == False:
        time.sleep(sleeptime)
        hand = input('What is your hand? ')
        
        if hand in okhands:
            comphand = random.choice(okhands)
            print('')
            print('You threw', hand, 'and I threw', comphand, ".")
            time.sleep(sleeptime)
            
            if okhands.index(hand) == okhands.index(comphand):
                print('')
                print('Nobody wins.')
            elif okhands.index(hand) == okhands.index(comphand)+1 or okhands.index(hand) == okhands.index(comphand)-2:
                print('')
                print('You win. Congratulations!')
            elif okhands.index(hand) == okhands.index(comphand)-1 or okhands.index(hand) == okhands.index(comphand)+2:
                print('')
                print('I win. YEAH!')           
        else:
            time.sleep(sleeptime)
            print('')
            print('I did not understand...')
            playgame()
        time.sleep(sleeptime)
        quitnow()        

print('Welcome to "Rock, Paper, Scissors"')
time.sleep(sleeptime)
print('')
print('You can throw one of three hands: "Rock", "Paper" or "Scissors"')

playgame()



    
        

    
    
 