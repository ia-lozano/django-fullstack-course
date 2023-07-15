###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# First Importa random module
import random as rd

# Generating a list of digits from 0 to 9
digits = list(range(10))

# Shuffling the digits
rd.shuffle(digits)

# Getting a 3 digit number out of the first 3 elements of the shuffled digits
number = digits[:3]

# Creating a string with the 3 digits because it's not possible to
# iterate through an integer
str_number = ''
for i in number:
    str_number += str(i)

# Writing core function
def guessCheck(a, b):
    '''
    This function compares the string a and b:
    1. If the position of any of the digits match
    2. If the string a contains a digit that is in string b, but in different position
    3. None of the above
    '''
    if a[0] == b[0] or a[1] == b[1] or a[2] == b[2]:
        print('Match')
    elif a[0] in b or a[1] in b or a[2] in b:
        print('Close')
    else:
        print('Nope')

# Starting an infinite loop (it breaks when strings a and b are equal (guess == str_number))
game_on = True
while game_on:
    guess = input("What's your guess? ")
    # Win condition
    if guess == str_number:
        print('You won!, the number is ', str_number)
        game_on = False
    # Checking guess
    else:
        guessCheck(guess, str_number)





            
