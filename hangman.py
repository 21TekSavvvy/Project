import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-'in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letter)>0:
        print('You have used these letters: ', ' '.join(used_letters) )

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a Letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
        elif user_letter in used_letters:
            print('You have already used that character. Please ty again!')

        else:
            print ('Invalid character!')
hangman()
