"""write a small function that ask the user to type a text and then display to the user the statistics of his/her typing. 
The statistics should contain the below elements :

1/ The total number of characters inside his/her typing.
2/ The list of characters used inside his/her typing.
3/ A dictionary in which each pair represents a character with its occurrences.
4/ The dictionary in which each pair represents a character with a tuple composed of its attributes above (occurrnces and parity). 
5/ Alternate the position of occurences and parity while building that latest dictionary. 
For the first pair, if you use (occurrence, parity) then for the next you should use (parity, occurrence).

--- Example

+ User input : try to solve that challenge - just get a try 0004.

--- Expected output :

+ number of characters : 50
+ list of characters : ['t', 'r', ' ', 'o', 's', 'l', 'v', 'e', 'h', 'a', 'n', 'g', '-', 'j', 'u', 'y', '0', '4', '.']
+ dictionary of occurences : {'t':6 , 'r':2, ' ':10, 'o':2, 's':2, 'l':3, 'v':1, 'e':4, 'h':2, 'a':3, 'n':1, 'g':2, '-':1, 'j':1, 'u':1, 'y':2, '0':3, '4':1, '.':1}
+ dictionary of attributes : {'t':(6, 'even') , 'r':('even',2), ' ':(10, 'even'), 'o':('even',2), 's':(2,'even'), 'l':('odd',3), 'v':(1,'odd'), 'e':('even',4), 'h':(2,'even'), 'a':('odd',3), 'n':(1,'odd'), 'g':('even',2), '-':(1,'odd'), 'j':('odd',1), 'u':(1,'odd'), 'y':('even',2), '0':(3,'odd'), '4':('odd',1), '.':(1,'odd')}

"""

txt = input('Please type something: ')

#1/ The total number of characters inside his/her typing.
txt_len = len(txt)
print('1/ The total number of characters inside his/her typing: ', txt_len)

#2/ The list of characters used inside his/her typing
word_set= set(txt)
print('2/ The list of characters used inside his/her typing (i.e. a set): ', word_set)

word_list=list(txt)
print('2/ The list of characters used inside his/her typing: ', word_list)

#3/ A dictionary in which each pair represents a character with its occurrences.
k = ()
v = 0
d = {}
for k in list(txt):
    if k in d:
        d[k] += 1
    else: d[k] = 1
print('3/ A dictionary in which each pair represents a character with its occurrences: ', d)

#4/ The dictionary in which each pair represents a character with a tuple composed of its attributes above (occurrnces and parity).


def determine_parity(d_f):
    for k,v in d_f.items():
        i=1
        if v%2 == 0:
            d_f_result[k] = v,'even'
        else:
            d_f_result[k] = v,'odd'
    return d_f_result[k]
        
         
d_f_result = {}
d_f_result_5 = {}


#5/ Alternate the position of occurences and parity while building that latest dictionary.
def determine_parity_5(d_f_5):
    i=0
    for k,v in d_f_5.items():
        i += 1
        if i%2 == 0:
            if v%2 == 0:
                d_f_result_5[k] = v,'even'
            else:
                d_f_result_5[k] = v,'odd'
                
        else:
            if v%2 == 0:
                d_f_result_5[k] = 'even', v
            else:
                d_f_result_5[k] = 'odd', v
    
    return d_f_result_5[k]

determine_parity(d)
print('4/ The dictionary in which each pair represents a character with a tuple composed of its attributes above (occurrences and parity): ', d_f_result)

determine_parity_5(d)
print('5/ Alternate the position of occurences and parity while building that latest dictionary:', d_f_result_5) 


