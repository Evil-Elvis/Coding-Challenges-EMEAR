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

# global variables

dict_of_chars_occurences = {}

def no_of_char(txt):
    txt_len = len(txt)
    return txt_len

def list_of_char(txt):
    word_set = set(txt)
    list_set = list(word_set)
    return list_set

def dict_char_occ(txt):
    k = ()
    v = 0
    d = {}
    for k in list(txt):
        if k in d:
            d[k] += 1
        else:
            d[k] = 1
    return(d)

def determine_parity_1(det_par):
    #local variable
    dic_det_par = {}

    for k, v in det_par.items():
        if v % 2 == 0:
            dic_det_par[k] = v, 'even'
        else:
            dic_det_par[k] = v, 'odd'
    return dic_det_par

def determine_parity_2(det_par_2):
    #local variables
    i = 0
    dic_det_par_2 = {}

    for k, v in det_par_2.items():
        i += 1
        if i % 2 == 0:
            if v % 2 == 0:
                dic_det_par_2[k] = v, 'even'
            else:
                dic_det_par_2[k] = v, 'odd'
        else:
            if v % 2 == 0:
                dic_det_par_2[k] = 'even', v
            else:
                dic_det_par_2[k] = 'odd', v

    return dic_det_par_2


def main():
    try:
        global dict_of_chars_occurences
        # define global variables
        txt = 'try to solve that challenge - just get a try 0004.'
        dict_txt = {}

        # call functions
        # 1/ The total number of characters inside his/her typing.
        sol_1 = no_of_char(txt)
        print('1/ The total number of characters inside his/her typing: ', sol_1)

        # 2/ The list of characters used inside his/her typing
        sol_2 = list_of_char(txt)
        print('2/ The list of characters used inside his/her typing (i.e. a set): ', sol_2)

        # 3/ A dictionary in which each pair represents a character with its occurrences.
        dict_of_chars_occurences = dict_char_occ(txt)
        print('3/ A dictionary in which each pair represents a character with its occurrences: ', dict_of_chars_occurences)

        # 4/ The dictionary in which each pair represents a character with a tuple composed of its attributes above (occurrnces and parity).
        sol_4 = determine_parity_1(dict_of_chars_occurences)
        print('4/ The dictionary in which each pair represents a character with a tuple: ', sol_4)

        # 5/ Alternate the position of occurences and parity while building that latest dictionary.
        sol_5 = determine_parity_2(dict_of_chars_occurences)
        print('5/ Alternate the position of occurences and parity while building that latest dictionary:', sol_5)

    except Exception as err:
        print("something went wrong - errmsg : ", err)

if __name__ == '__main__':
    main()
