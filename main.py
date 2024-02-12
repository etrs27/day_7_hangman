from replit import clear
import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(hangman_art.logo)

#Create blanks
display = []
for _ in range(word_length):
  display += "_"

while not end_of_game:
  guess = str(input("Guess a letter:")).lower()
  clear()

  if guess in display:
    print(f"You have already guessed the letter {guess}.")

  #Check guessed letter
  for index in range(word_length):
    letter = chosen_word[index]
    if letter == guess:
      display[index] = letter

  #Check if user is wrong.
  if guess not in chosen_word:
    print(f"You have guessed incorrectly. The letter {guess} is not in the word.")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose.")

  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  #Check if user has got all letters.
  if "_" not in display:
    end_of_game = True
    print("You win.")

  print(hangman_art.stages[lives])