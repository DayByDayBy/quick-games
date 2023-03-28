import random
import string
from words import words

def get_word(words):
    word = random.choice(words)  # selcting random word from wordlist to match against guesses
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.lower()

def hangman():
    word = get_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()

    chances = 9

    while len(word_letters) > 0 and chances > 0:
        print('you have', chances, 'chances left, and so far have guessed: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('so far you have: ', ' '.join(word_list))

        user_letter = input('guess a letter: ').lower() 
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters: 
                word_letters.remove(user_letter)
                print('')
            else:
                chances -= 1
                print('\nyour letter, ', user_letter, 'is not in the word.')
        
        elif user_letter in used_letters:
            print('oops! You already guessed that one.')
        else:
            print("hey, that's not a letter!")
    if chances == 0:
        print ('you have run out of chances, you lose! the word was', word, '!')
    else:
        print('you win! the word was', word, '!')

if __name__ == '__main__':
    hangman()


