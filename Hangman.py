import random
from hangman_art import *
from hangman_words import word_list
from os import system, name
from time import sleep

# Function for clear screen
def clear():
  
    # For windows
    if name == 'nt':
        _ = system('cls')
  
    # For mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


chosen_word = random.choice(word_list)    #chosen_word = word_list[random.randint(0, len(word_list)-1)]
word_length = len(chosen_word)

end_of_game = False
lives = 6

# HANGMAN logo
print(logo)

# testing code
print(f'Pssst, the solution is {chosen_word}.')

# create blanks
display = []
already_guessed_letters = []
for i in range(len(chosen_word)):
    display.append("_")     #display += "_"


while not end_of_game:
    # Clear screen
    sleep(3)
    clear()

    # Input from player
    print(f"{' '.join(display)}")
    guess= input("\nGuess a letter: ").lower()

    # Check for already guessed letters
    if guess in already_guessed_letters:
        print("Letter is already guessed. Try again.")
        continue
    already_guessed_letters += guess

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")

        # Filling gaps incase of correct guess
        if letter == guess:
            display[position] = letter

    # Check if player is wrong
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"Your guessed letter '{guess}' is not in the word. You lose a life!")

        print(f"Remaining Lives = {lives}")
        if lives == 0:
            print("You lose! \nThe word was = "+ chosen_word)
            print("HANGMAN!!! \nBetter luck next time.")
            #print(stages[lives]+"\n HANGMAN!!!")
            break
    else:
        print("HOORAYY! You guessed it right!")

    # Join all the elements in the list
    print(f"{' '.join(display)}")

    # check if user has got all the letters
    if "_" not in display:
      end_of_game = True
      print("You WIN!!")

