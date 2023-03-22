import random
import hangman_words
import hangman_art
end_of_game = False
word_list = hangman_words
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = len(hangman_art.stages)
display = []
print(hangman_art.logo)

for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}")
wrong_guess_list=[]
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word and guess not in wrong_guess_list:

        print(f"the letter {guess} isn't in the word")
        lives -= 1
        print(hangman_art.stages[lives])
    if guess not in wrong_guess_list:
        wrong_guess_list.append(guess)
    elif guess in wrong_guess_list:
        print(f"you alrady try the letter {guess.upper()}")
    if lives == 0:
        end_of_game = True
        print("you loose")


    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")