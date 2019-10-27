import random

def checkifsame(lst):
    '''If any list contains three ones, twos, or threes, the function will return true'''
    if lst.count(1) ==3:
        return True
    elif lst.count(2)==3:
        return True
    elif lst.count(3)==3:
        return True
    else:
        return False

f = True
while f == True:                #While the user chooses 'y'
    round = 1
    player1list = random.sample(range(1, 4), 3)
    human_list = random.sample(range(1, 4), 3)          #Creates three lists of random numbers between 1, 3 with no repeats
    player2list = random.sample(range(1, 4), 3)
    print('Welcome to Card game:')
    print('Number of players is 3 and total cards for each player are 3')
    print('Lets shuffle the cards')
    print('We have 2 AI players and 1 Human player')
    print('Player 1 AI Cards:' ,player1list)
    print('Player Human Cards:', human_list)
    print('Player 2 AI Cards:' ,player2list)
    while True:
        print('Round: %s' %(round))
        print('=' * 20)
        aichoice1 = random.randint(0, 2)
        print('Player1 AI decision is %d' %(aichoice1 + 1))         #AI 1 chooses random "card" from the human player and adds it to its list
        player1list.append(human_list.pop(aichoice1))
        print('Player1 cards:', player1list)
        print('Human cards:' ,human_list)
        print('Player2 cards:' ,player2list)
        if checkifsame(player1list) == True:            #If the AI has three of the same cards, the loop will end
            break
        print()
        print('Human turn')
        print('Enter 1 for card 1')
        print('Enter 2 for card 2')
        print('Enter 3 for card 3')
        humanchoice = int(input()) - 1
        human_list.append(player2list.pop(humanchoice))             #Human chooses a card from the AI 2's list and adds it to his/her list
        print('Player 1 cards:', player1list)
        print('Human cards:' ,human_list)
        print('Player 2 cards:' ,player2list)
        if checkifsame(human_list) == True:     #If the human has three of the same cards, the loop will end
            break
        print()
        aichoice2 = random.randint(0, 2)
        print('Player2 AI decision is %d' % (aichoice2 + 1))
        player2list.append(player1list.pop(aichoice2))          #AI 2 chooses a random card from AI 1's list and adds it to its list
        print('Player1 cards:', player1list)
        print('Human cards:', human_list)
        print('Player2 cards:', player2list)
        if checkifsame(player2list) == True:                #If the AI has three of the same cards, the loop will end
            break

        round += 1                      #Increase the round every time a winner isn't decided

    if checkifsame(player1list) == True:
        print('Player1 Won!')
        print('Thanks for playing')
    elif checkifsame(human_list) == True:               #If any player has three of the same cards (checkifsame == True), announce that the player won
        print('Human Won!')
        print('Thanks for playing')
    elif checkifsame(player2list) == True:
        print('Player2 Won!')
        print('Thanks for playing')

    choice = 'ko'
    choice = choice.upper()
    while choice != 'Y' and choice != 'N':
        choice = input('Do you want to play again: Y/N')            #Ask if the user wants to play again - does not accept invalid inputs
        choice = choice.upper()
        if choice == 'Y':
            f = True
        elif choice == 'N':
            print('Goodbye')                    #Say goodbye
            f = False
        else:
            print('Invalid input')