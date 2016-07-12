import sys
import re
# import ipdb


def find_first_common_letter(str1, str2):
    res = [len(str1), len(str2)]
    for i, c1 in enumerate(str1):
        for n, c2 in enumerate(str2):
            if c1 == c2:
                if n < res[1]:
                    res = [i, n]
    if res[0] != len(str1):
        return res
    else:
        return None


def find_common_letters(str1, str2):
    letter_couples = []
    for i, c1 in enumerate(str1):
        for n, c2 in enumerate(str2):
            if c1 == c2:
                letter_couples.append([i, n])
    return letter_couples


def find_first_couples(letter_couples):
    smallest_1 = None
    smallest_2 = None
    min_ind_1 = sys.maxint
    min_ind_2 = sys.maxint
    smallest_possible = []
    for couple in letter_couples:
        if couple[0] <= min_ind_1:
            min_ind_1 = couple[0]
            smallest_1 = couple
        if couple[1] <= min_ind_2:
            min_ind_2 = couple[1]
            smallest_2 = couple
    for couple in letter_couples:
        if not_larger(couple, smallest_1):
            smallest_possible.append(couple)
        if not_larger(couple, smallest_2):
            smallest_possible.append(couple)
    return smallest_possible


def not_larger(couple, base):
    return couple[0] < base[0] or couple[1] < base[1]


def find_next_common(str1, str2, pref, list_of_common):
    couples = find_common_letters(str1, str2)
    couples = find_first_couples(couples)

    for couple in couples:
        print couple
        char = str1[couple[0]]
        str1 = reminder_by_index(str1, couple[0])
        str2 = reminder_by_index(str2, couple[1])
        find_next_common(str1, str2, pref + char, list_of_common)

    if (not couples) and (pref not in list_of_common):
        list_of_common.append(pref)


# def find_next_common(str1, str2, pref, list_of_common):
#     # if str1 == "" or str2 == "":
#     #     if pref not in list_of_common:
#     #         list_of_common.append(pref)
#     #     return True
#     res1 = find_first_common_letter(str1, str2)
#     res2 = find_first_common_letter(str2, str1)
#     # print "0"
#     if res1:
#         char = str1[res1[0]]
#         if res1[0] < res2[1] and res1[1] < res2[0]:
#             print "1"
#             str1 = reminder_by_index(str1, res1[0])
#             str2 = reminder_by_index(str2, res1[1])
#             find_next_common(str1, str2, pref + char, list_of_common)
#         elif res1[0] > res2[1] and res1[1] > res2[0]:
#             print "2"
#             str1 = reminder_by_index(str1, res2[1])
#             str2 = reminder_by_index(str2, res2[0])
#             find_next_common(str1, str2, pref + char, list_of_common)
#         elif res1[0] == res2[1] and res1[1] == res2[0]:
#             # print "3"
#             str1 = reminder_by_index(str1, res1[0])
#             str2 = reminder_by_index(str2, res1[1])
#             find_next_common(str1, str2, pref + char, list_of_common)
#         else:
#             # print "4"
#             str11 = reminder_by_index(str1, res1[0])
#             str21 = reminder_by_index(str2, res1[1])
#             str12 = reminder_by_index(str1, res2[1])
#             str22 = reminder_by_index(str2, res2[0])
#             find_next_common(str11, str21, pref + char, list_of_common)
#             find_next_common(str12, str22, pref + char, list_of_common)
#     else:
#         if pref not in list_of_common:
#             list_of_common.append(pref)
#         return True


def reminder_by_char(string, char):
    ind = string.find(char)
    return string[ind + 1:]


def reminder_by_index(string, index):
    if index < len(string):
        return string[index + 1:]
    else:
        return ""


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


def process_line(string):
    regex = re.compile("(.+?);(.+?):'(.+?)'")
    try:
        string1 = regex.match(string).group(1)
        string2 = regex.match(string).group(2)
        result = regex.match(string).group(3)
    except AttributeError:
        return ""
    res1 = ""
    res2 = ""
    res = ""
    for i, c in enumerate(result):
        ind1 = string1.find(c)
        ind2 = string2.find(c)
        if ind1 > ind2:
            padd1 = ""
            padd2 = " " * (ind1 - ind2)
            pos = ind1
        else:
            padd1 = " " * (ind2 - ind1)
            padd2 = ""
            pos = ind2
        res1 = "".join([res1, string1[:ind1] + padd1 + "|" + c])
        res2 = "".join([res2, string2[:ind2] + padd2 + "|" + c])
        res = "".join([res, pos * " " + "|" + c])
        string1 = reminder_by_char(string1, c)
        string2 = reminder_by_char(string2, c)
        if i == len(result) - 1:
            res1 = "".join([res1, string1[ind1:]])
            res2 = "".join([res2, string2[ind2:]])
    return res1 + '\n' + res2 + '\n' + res + "\n"


def main():
    with open(sys.argv[1], 'r') as test_cases, open("result.txt", 'w') as result_file:
        for test in test_cases:
            if test[-1] == "\n":
                test = test[:-1]
            if test != "":
                [str1, str2] = test.split(";")
                result = find_longest_common_string(str1, str2)
                print "%s:'%s'" % (test, result)
                result = "%s:'%s'" % (test, result)
                result = process_line(result)
                result_file.write(result)

if __name__ == '__main__':
    main()
