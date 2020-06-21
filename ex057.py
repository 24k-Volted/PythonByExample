#####
# Python By Example
# Exercise 057
# Christopher Hagan
#####

import random

randomNumber = random.randint(1, 10)
guess = 0
while guess != randomNumber:
    guess = int(input('Guess the computer\'s random number between 1 and 10: '))
    if guess < randomNumber:
        print('Too low!')
    elif guess > randomNumber:
        print('Too high!')

print('Correct, the computer\'s number was {}'.format(randomNumber))
