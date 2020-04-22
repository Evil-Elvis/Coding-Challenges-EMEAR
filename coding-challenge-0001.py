random_number = (0)
sum_of_digits = (0)
product_of_digits = (0)

# import random module
from random import randint

random_number = randint(10,99)

# convert integer into str in order to select first and second digit and convert each digit back to integer
random_number_str = str(random_number)
digit_1 = int(random_number_str[0])
digit_2 = int(random_number_str[1])

# counter for number of trials
number_of_guesses = 1

# calculations
sum_of_digits = digit_1 + digit_2
product_of_digits = digit_1 * digit_2

# Player interaction
print('Your task is to guess a number between 10 and 99 based on the sum and product of the two digits.', '\n', 'Enter "0" to exit.') 
print('Sum of digits: ', sum_of_digits)
print('Product of digits: ', product_of_digits)


# while loop repeats until it breaks due to correct user entry or entering "0". 
while True:
    guess = int(input('Guess the random_number: '))
    if guess == random_number:
        print('Congratulations! {} is the correct number! You needed {} attempts.'.format(random_number, number_of_guesses))
        break
    elif guess == 0:
        break
    elif guess < random_number:
        print('random_number is larger')
        number_of_guesses += 1
    else:
        print('random_number is smaller')
        number_of_guesses += 1
