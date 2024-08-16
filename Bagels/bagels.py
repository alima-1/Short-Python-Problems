""" Bagels by Al Sweigart
A deductive logic game where you must guess a number based on the clues.
"""
import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def getSecretNum():
    '''Returns a string made up of NUM_DIGITS unique random numbers'''
    #the string is converted to a list bse strings are immutable and the
    #shuffle method mutates a sequence in-place.
    numbers = '0123456789'
    secretNum = random.sample(numbers,k=3)
    return ''.join(secretNum)

def main():
    print(f'''Bagels, a deductive logic game.
    By Al Sweigart.

    I am thinking of a {NUM_DIGITS}-digit with no repeated digits.
    Try to guess what it is. Here are some clues:
    When i say:    That means:
      Pico         One digit is correct but in the wrong position
      Fermi        One digit is correct and in the right place.
      Bagels       No digit is correct.

    For example, if the secret number was 248 and your guess was 843, the 
    clues would be Fermi Pico.''')


    while True: #the loop the iterates the game 
        secretNum = getSecretNum()#stores the secret number the player needs to guess
        print('I have thought up a number.')
        print(f'You have {MAX_GUESSES} guesses to get it.')

        numGuesses = 1 # keeps count of the number of guesses 
        while numGuesses < MAX_GUESSES: #
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{numGuesses}')
                guess = input('>')
        
            clues = getClues(guess,secretNum)
            print(clues)
            numGuesses+=1
            
            if guess == secretNum:
                 break
            if numGuesses >= MAX_GUESSES:
                print(f'You run out of guesses \n The answer was {secretNum}')
    
    
        print("Do you want to play againg? (Yes or No)")
        if not input('>').lower().startswith('y'):
            break

    print('Thanks for playing!')



def getClues(guess,secretNum):
    if guess == secretNum:
        return 'You got it'
  
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)            
           

if __name__ == '__main__':
    main()        
