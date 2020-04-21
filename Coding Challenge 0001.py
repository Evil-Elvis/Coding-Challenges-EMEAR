"""
Open your PyCharm Or IDLE any Editor of your preference
Declare three variables named random_number and sum_of_digits and product_of_digits.
Initialize these variables with 0 since they will contain integers [numbers].
Then instruct the Python Interpreter to randomly choose a value of two digit between 10 & 99. 
Save that random value into the appropriate variable (random_number).
Compute the sum of digits inside this random number and save it into sum_of_digits.
Compute the product of all digits inside this number and save into product_of_digits.
Display the two result to the user and prompt the user to imagine/guess and type this random number.
Compare this number with the random value and inform the user either it is higher or lower or equal.
In event the user number matches with the random number then congrats the user :)
"""

random_number = (0)
sum_of_digits = (0)
product_of_digits = (0)

from random import randint

random_number = (randint(10,99))
random_number_str = str(random_number)
digit_1 = int(random_number_str[0])
digit_2 = int(random_number_str[1])

sum_of_digits = digit_1 + digit_2
product_of_digits = digit_1 * digit_2

print(sum_of_digits)
print(product_of_digits)

while True:
    guess = int(input('Guess the random_number: '))
    if guess == random_number:
        print('Congratulations! {} is the correct number!'.format(random_number))
        break
    elif guess < random_number:
        print('random_number is larger')
    else:
        print('random_number is smaller')