"""
Name(s): Ayan
Name of Project: Rock Paper Scissors
"""

#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4


import random

pos = ['Rock', 'Paper', 'Scissors' ]
print('Rock Paper Scissors v1.0')
botscore = 0
score = 0
playagain = 'y'
while str(playagain) == 'y':
  print('\nYou:' + str(score) + ' Bot:' + str(botscore) + '\nType "Rock", "Paper", or "Scissors".\n')
  wincon = None
  selection = input()
  if (selection != 'Rock') and (selection != 'Paper') and (selection != 'Scissors'):
    print('Error: Invalid selection.')
    continue
  botsel = random.choice(pos)
  print('You chose:' + str(selection) + '\nEnemy chose:' + str(botsel))
  if (botsel == 'Rock' and selection == 'Paper') or (botsel == 'Paper' and selection == 'Scissors') or (botsel == 'Scissors' and selection == 'Rock'):
   wincon = True
  elif (botsel == 'Paper' and selection == 'Rock') or (botsel == 'Scissors' and selection == 'Paper') or (botsel == 'Rock' and selection == 'Scissors'):
    wincon = False
  else:
    wincon = None
  if wincon == True:
    print('You win!')
    score = score + 1
  elif wincon == False:
    print('Bot wins!')
    botscore = botscore + 1
  else:
    print('Tie!')
  playagain = input('Play again? (y/n):')

if score > botscore:
  print('Congratulations, you won!')
elif botscore > score:
  print('The bot won it all!')
else:
  print("It's a tie!")