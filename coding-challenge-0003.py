"""
Open your PyCharm Or IDLE or your favourite Code Editor. Create a function named func_single_multiplication. 
It should take as input a parameter called number, then it should display the multiplication table (from 1 to 10) of this number. 
For the display - use any beautiful creative style you want.

Create another function called func_many_multiplication. 
It should take as input a parameter called number and will display the multiplication table of each number from 1 to that input parameter. 
For instance, if input number is 4, then it should display the table of 1, 2, 3 and 4.

Please notice that the function called func_many_multiplication should use the first function called func_single_multiplication.
"""

def func_single_multiplication(number):
    for i in range(1,11):
        print('{} x {} = '.format(i, number), i*number)
        
func_single_multiplication(int(input('Enter number: ')))

def func_many_multiplication(number):
    for i in range(1,number+1,1):
        func_single_multiplication(i)
        print('\n')

func_many_multiplication(int(input('Enter number for many multiplication tables: ')))

# create a dictionary with number as key and results of multiplication as values. 
# Problem: only one value (result of number x 10) is returned, not a list of the 10 multiplications

dict={}
def func_single_multiplication2(number):
    for i in range(1,11):
        v= i*number
        dict[number] = v
    return(dict)



func_single_multiplication2(int(input('Enter number: ')))
print(dict)
