import sys


def find_common_letters(str1, str2):
    """ Tested properly """
    letter_couples = []
    for i, c1 in enumerate(str1):
        for n, c2 in enumerate(str2):
            if c1 == c2:
                letter_couples.append([i, n])
    return letter_couples


def not_larger(couple, base):
    """ Tested properly """
    return couple[0] < base[0] or couple[1] < base[1]


def find_first_couples(letter_couples):
    """ TODO: Tested partially """
    smallest_1 = None
    smallest_2 = None
    min_ind_1 = sys.maxint
    min_ind_2 = sys.maxint
    for couple in letter_couples:
        if couple[0] <= min_ind_1:
            min_ind_1 = couple[0]
            smallest_1 = couple
        if couple[1] <= min_ind_2:
            min_ind_2 = couple[1]
            smallest_2 = couple
    return [smallest_1, smallest_2]


def filter_unnecessary_couples(letter_couples):
    smallest_1 = None
    smallest_2 = None
    [smallest_1, smallest_2] = find_first_couples(letter_couples)
    smallest_possible = []
    smallest_possible.append(smallest_1)
    if smallest_1 != smallest_2:
        smallest_possible.append(smallest_2)
    for couple in letter_couples:
        if not_larger(couple, smallest_1):
            if couple not in smallest_possible:
                smallest_possible.append(couple)
        if not_larger(couple, smallest_2):
            if couple not in smallest_possible:
                smallest_possible.append(couple)
    return smallest_possible


def reminder_by_index(string, index):
    """ Tested properly """
    if index < len(string):
        return string[index + 1:]
    else:
        return ""


def find_next_common(str1, str2, pref, list_of_common):
    couples = find_common_letters(str1, str2)
    if couples:
        couples = filter_unnecessary_couples(couples)
        for couple in couples:
            try:
                char = str1[couple[0]]
            except:
                char = ''
            str1_new = reminder_by_index(str1, couple[0])
            str2_new = reminder_by_index(str2, couple[1])
            find_next_common(str1_new, str2_new, pref + char, list_of_common)
    if pref not in list_of_common and pref:
        list_of_common.append(pref)

def find_longest_common_string(str1, str2):
    list_of_new = []
    for i, _ in enumerate(str1):
        for n, _ in enumerate(str2):
            find_next_common(str1[i:], str2[n:], "", list_of_new)
    longest = ""
    for lcs in list_of_new:
        if len(lcs) > len(longest):
            longest = lcs
    return longest


def main():
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            if test[-1] == "\n":
                test = test[:-1]
            if test != "":
                [str1, str2] = test.split(";")
                result = find_longest_common_string(str1, str2)
                print result

if __name__ == '__main__':
    main()
