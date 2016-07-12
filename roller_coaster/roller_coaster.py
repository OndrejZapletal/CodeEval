import sys

def convert_string(string):
    alter = True
    new_string  = ""
    for c in string:
        if c.isalpha():
            if alter:
                c = c.upper()
                alter = not alter
            else:
                c = c.lower()
                alter = not alter
        new_string = new_string + c
    return new_string


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test[-1] == '\n':
            test = test[:-1]
        if test != "":
            print(convert_string(test))
