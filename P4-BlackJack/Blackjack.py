import random
import gameArt

from gameArt import logo
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#cards = [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]
ACE = 11
playerBustStatus = False
computerBustStatus = False

player = []
computer = []

def dealCards():
    randomCard = cards[random.randint(0, 12)]
    return randomCard

def calculator(val1, val2):
    sum = val1 + val2
    return sum


def checkAce(checkCard):
    """Check is Ace is present in hand and if so how many.
    Takes list as an arguement.
    First result returns if ace is present or not (boolean).
    Second result returns the number of ace present in a hand."""
    aceCount = 0
    for card in checkCard:
        if card == 11:
            aceFound = True
            aceCount = aceCount + 1
            #print("Ace FOUND")
        else:
            aceFound = False
            #print("NOT FOUND")
    return aceCount

# dealing inital cards
for i in range(0,2):
    player.append(dealCards())
    computer.append(dealCards())

# Computer initial status
print(f"Computer's second card: {computer[1]}")
computerAceCount = checkAce(computer)
#print(computerAceCount)

# Player initial status
playerAceCount = checkAce(player)
#print(playerAceCount)

# print("Player:")
# aceStatus = checkAce(player)
# print(f"Ace Found: {aceStatus[0]}, Ace Count: {aceStatus[1]}")
# print("computer:")
# checkAce(computer)

playerSumCards = calculator(player[0], player[1])
print(f"Player cards:{player}, Sum: {playerSumCards}")
print()

### USER LOGIC START ###
print("*** PLAYER PLAYING ***")
# check is there are two aces at start, 
# if yes, convert one ace to 1. soft 12
if playerSumCards > 21 and playerAceCount == 2:
    player[-1] = 1
    playerSumCards = calculator(player[0], player[1])
    print(f"cards:{player}, sum: {playerSumCards}")


playAgain = True
while playAgain:
    print()
    print()
    hitCard = input("hit? 'y' or 'n': ")
    if hitCard == 'y':
        player.append(dealCards())
        playerSumCards = calculator(playerSumCards, player[-1])     # player[-1] = gets the last element
        playerAceCount = checkAce(player)
        print(f"cards:{player}")
        print(f"sum: {playerSumCards}")
        #print(f"sum: {playerSumCards}, ace count: {playerAceCount}")
        # check if (great than 21 and ace present) then convert ace to 1
        if playerSumCards > 21:
            # look for ace then convert to 1
            if playerAceCount > 0:
                for card in player:
                    if ACE in player:
                        acePosition = player.index(ACE)
                        player[acePosition] = 1
                        break

                playerSumCards = 0
                for i in range(0, len(player)):
                    playerSumCards = calculator(playerSumCards, player[i])
                    print(f"curent sum: {playerSumCards}")
                print(f"cards:{player}")
                print(f"sum: {playerSumCards}")

                if playerSumCards > 21:
                    playerBustStatus = True
                    playAgain = False
                    print("BUST")
            else:        
                playerBustStatus = True
                playAgain = False
                print("BUST")
    else:
        playAgain = False
        
print()

### COMPUTER LOGIC ###
print("*** DEALER PLAYING ***")
print()

computerSumCards = calculator(computer[0], computer[1])
print(f"cards:{computer}, Sum: {computerSumCards}")

if computerSumCards > 21 and computerAceCount == 2:
    computer[-1] = 1
    computerSumCards = calculator(computer[0], computer[1])
    print(f"cards:{computer}, Sum: {computerSumCards}")

computerPlayAgain = True
while computerPlayAgain and computerSumCards < 17 and computerSumCards < playerSumCards and not playerBustStatus:
    print()
    print()

    computer.append(dealCards())
    computerSumCards = calculator(computerSumCards, computer[-1])     # player[-1] = gets the last element
    computerAceCount = checkAce(computer)
    print(f"cards:{computer}")
    print(f"sum: {computerSumCards}")
    #print(f"sum: {computerSumCards}, ace count: {computerAceCount}")
    
    # check if (great than 21 and ace present) then convert ace to 1
    if computerSumCards > 21:
        # look for ace then convert to 1
        if computerAceCount > 0:
            for card in computer:
                if ACE in computer:
                    acePosition = computer.index(ACE)
                    computer[acePosition] = 1
                    break

            computerSumCards = 0
            for i in range(0, len(computer)):
                playerSumCards = calculator(computerSumCards, computer[i])
                print(f"curent sum: {computerSumCards}")
            print(f"cards:{computer}")
            print(f"sum: {computerSumCards}")


            if playerSumCards > 21:
                computerBustStatus = True
                computerPlayAgain = False
                print("BUST")

        else:        
            computerBustStatus = True
            computerPlayAgain = False
            print("BUST")

    else:
        computerPlayAgain = False

print()
print()
print("*** GAME OVER ***")
### WIN LOGIC ###
# bust conditions
if playerBustStatus and not computerBustStatus:
    print("Dealer WINS")
elif computerBustStatus and not playerBustStatus:
    print("Player WINS")
# sum condition
elif computerSumCards > playerSumCards:
    print("Dealer WINS")
elif playerSumCards > computerSumCards:
    print("Player WINS")
# draw condition
else:
    print("DRAW")



