import random

INFO = {0: '石头', 1: '剪刀', 2: '布'}

computer = random.randint(0, 2)
player = eval(input(">>"))

if computer == player:
    print('ping')
elif player-computer == -1 or player-computer == 2:
    print('player win')
else:
    print('computer win')

