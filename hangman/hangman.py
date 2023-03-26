import random
import string
import pygame          
from words import words
from weeGuy_ASCII import hanged_man

pygame.init()


def get_word(words):
    word = random.choice(words)  # selecting random word from wordlist to match against guesses
    while '-' in word or ' ' in word:  # removing words in list that are hyphenated or contain spaces
        word = random.choice(words)  # selecting word after removing hyphenated etc words
    return word.lower()

def hangman():
    word = get_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()

    chances = 7

    while len(word_letters) > 0 and chances > 0:
        print('you have', chances, 'chances left, and so far have guessed: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(hanged_man[chances])
        print('so far you have: ', ' '.join(word_list))

        user_letter = input('guess a letter: ').lower() 
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters: 
                word_letters.remove(user_letter)
                print('')
            else:
                chances -= 1
                print('\nyour letter, ', user_letter, 'is not in the word.\n')
        
        elif user_letter in used_letters:
            print('\noops! You already guessed that one.\n')
        else:
            print("\nhey, that's not a letter!\n")
    if chances == 0:
        print(hanged_man[chances])
        print ('\noh no, they died! the word was', word, '!\n')
    else:
        print('\nyou win! the word was', word, '!\n')

if __name__ == '__main__':
    hangman()



# user_input = input('type your guess here:  ')
# print(user_input)
    
    
    
    
    
    # game_word = get_word()
    # print(game_word)
    # guesses = 6
    # while guesses > 0:
    #     guess = input('Guess a letter: ')
    #     if guess in game_word:
    #         print('Good guess!')
    #         guesses -= 1
    #     else:
    #         print('Oops! That letter is not in my word.')
    #         guesses -= 1
    # if guesses == 0:
    #     print('You ran out of guesses. The word was', game_word) 
    