import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from a list of words, omitting special characters
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)

    #letters in the word
    word_letters = set(word) 

    #make a list of letters, letters must exist first before they can be guessed
    #injects ascii letters in uppercase into a set
    alphabet = set(string.ascii_uppercase)

    #a place to store what letters the user has guessed
    used_letters = set() 
    #get user input for their guess, and store it and convert to uppercase letters
    
    #Allows user to keep guessing until the man is hanged.
    #loop condition for game
    #letters in guessed word must be more than 0
    #game ends if lives reach zero
    #game ends if word is guessed
    #show user current word with correctly guessed letters and dashes for letters/
    #to be guessed 
    while len(word_letters) > 0:

        #show the correct letters guessed
        #show the letters to be guessed 
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current Word: ', ''.join(word_list))

        #show user what letters they have guessed
        print('Letters guessed ', ' '.join(used_letters))
        # show word with correctly guessed letters, and character '_' where letters are to be guessed


        user_letter = input('Guess a letter: ').upper()
        #check if users guessed letter exists in alphabet and test it vs letters the user has guessed
        if user_letter in alphabet - used_letters:
            #add the user letter to used letters 
            used_letters.add(user_letter)
            #test if user letter is in word held in memory
            if user_letter in word_letters:
                #removes letter from word held in memory
                word_letters.remove(user_letter)
        #
        elif user_letter in used_letters:
            print('letter already guessed, guess another letter')

        else: 
            print('invalid character')

hangman()