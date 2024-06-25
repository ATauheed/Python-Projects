import random
import Hangman_Words
import Hangman_art
import os

print(Hangman_art.logo)
print()

lives = 6

guessList = []      # list to keep track of the guessed letter

chosen_word = random.choice(Hangman_Words.word_list).lower()
wordLength = len(chosen_word)
#print(f"solution = {chosen_word}")

display = []        # list to display letters

for blank in range(wordLength):
    display.append("_")

gameOver = False    # indicator to decide if the game is over or not

# main logic
while not gameOver:
    
    print(f"WORD: {' '.join(display)}")   # joins the elements of display into one string (Look nicer)
    print(Hangman_art.stages[lives])
    #print(f"lives = {lives}")
    #print(f"Already guessed: {guessList}")
    
    guess = input("Chose a letter: ")
    guess = guess.lower()
    print()
    os.system('cls')    # clear the console/terminal
    
    if guess in guessList:
        print(f"You already guessed {guess}")
    else:
        guessList.append(guess)

        for position in range(wordLength):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print(f"{guess} is not in the word. You lose a life :p")
            lives = lives - 1
            if lives == 0:
                gameOver = True
                print(Hangman_art.stages[lives])
                #print(f"lives = {lives}")
                print("YOU LOSE!")


    if "_" not in display:
        gameOver = True
        print("YOU WIN!")

print(f"\nThe word was: {chosen_word} \n")
