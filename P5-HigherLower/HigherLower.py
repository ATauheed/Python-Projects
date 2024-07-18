from gameArt import logo
from gameArt import vs
from gameData import data
import random
import os


## formating data
def dataFormater(randomData):
    """Take the random data and returns the formated data"""
    accName = randomData["name"]
    accDescription = randomData["description"]
    accCountry = randomData["country"]
    return f"{accName}, a {accDescription}, from {accCountry}"

# check guess is correct or not
def checkAnswer(userGuess, followerA, followerB):
    """ Take the user guess and returns if the guess is correct or not"""
    if followerA > followerB:
        return userGuess == "a"
    else:
        return userGuess == "b"


print(logo)

score = 0
correctGuess = True
choiceB = random.choice(data)

while correctGuess:

    ## generate random data from "gameData" file
    choiceA = choiceB
    choiceB = random.choice(data)
    #print(choiceA)
    #print(choiceB)
    # makes sure if the choices are different
    while choiceA == choiceB:
        choiceB = random.choice(data)


    print(f"Compare A: {dataFormater(choiceA)}")
    print(vs)
    print(f"Against B: {dataFormater(choiceB)}")
    print()

    ## checking if the guess is correct
    followerCountA = choiceA["follower_count"]
    followerCountB = choiceB["follower_count"]

    print(f"A: {followerCountA}")
    print(f"B: {followerCountB}")

    # Asking the user to guess
    guess = input("How has more followers? Type 'A' or 'B': ").lower()

    isCorrect = checkAnswer(guess, followerCountA, followerCountB)

    os.system('cls')
    print(logo)

    if isCorrect:
        score = score + 1
        print(f"You are CORRECT! Your current score: {score}")
    else:
        correctGuess = False
        print(f"You are WRONG! Your final score: {score}")
    
    print()

    



