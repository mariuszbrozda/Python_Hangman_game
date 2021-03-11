import random
from hangman_art import stages, logo
from hangman_words import word_list
import os

#The clear() function imported from replit to clear the output between guesses.
def clear(): return os.system('clear')



# Printing Hangman logo on beginning of the game. 
print(logo)

# Set the variables
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []


# For loop used to iterate through chosen word lentgh to display _ in the places of letters 
# It shows user how many letter is included in word.
 
for _ in range(word_length):
    display += "_"



print(f"{' '.join(display)} \n")


# While loop is used to executing the code untill game_is_finished get True value
while not game_is_finished:
    guess = input("Guess a letter: ").lower()


    clear()

# Check if letter was guessed by user before.

    if guess in display:
        print(f"You've already guessed {guess}")

# For loop used to check if letter guessed by user is in word.
# If letter is in the word, it is displayed 
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

# Check if guessed letter is not in the word, user lose life if it's not in the word.
# If lives are equal to 0, user lose the game
# If user guess corectly all letters in word, game is finished and user wins.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")

    if not "_" in display:
        game_is_finished = True
        print("You win.")


# Printing hangman art stages according to number of lives.
    print(stages[lives])
