import sys
import string

def convert_column(column):
    reminder_list = ""
    it = 1
    while column:
        divider = 26 ** it
        difference = column % divider 
        if difference == 0:
            difference = divider
        column -= difference
        index = difference/(divider/26)
        reminder_list = alph(index) + reminder_list
        it += 1
    return reminder_list


def alph(index):
    return list(string.ascii_uppercase)[int(index)-1]


def ret_col_name(col_indx, itr):
    if col_indx:
        diff = col_indx % (26 ** itr)
        if not diff:
            diff = 26 ** itr
        return ret_col_name(col_indx - diff, itr + 1) + alph(diff / (26 ** (itr - 1)))
    else:
        return ""


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test[-1] == '\n':
            test = test[:-1]
        if test:
            print(ret_col_name(int(test), 1))
