# import time
import sys
import re
# import ipdb


def find_first_common_letter(str1, str2):
    res1 = [len(str1), len(str2), ""]
    for i, c1 in enumerate(str1):
        for n, c2 in enumerate(str2):
            if c1 == c2:
                if n < res1[1]:
                    res1[0] = i
                    res1[1] = n
                    res1[2] = c1
    return res1


def process_strings_from(i, n, string1, string2, result_list):
    find_string_forward(string1[i:], strin2[n:])
    find_string_backwards(string1[:i], strin2[:n])


def find_string_forward(string1, string2):
    list_of_strings = []
    prefix = ""
    for
    find_next()
    return list_of_strings


def find_string_backwards(string1, string2):
    list_of_strings = []
    return list_of_strings


def find_next(str1, str2, prefix, list_of_common):

    res1 = find_first_common_letter(str1, str2)

    if res1[2] != "":
        find_next_common(str1[res1[0]+1:], str2[res1[1]+1:], prefix + res1[2], list_of_common)
    else:
        if prefix not in list_of_common:
            list_of_common.append(prefix)
    return True


def find_prvious():


def find_next_common(str1, str2, prefix, list_of_common):
    if str1 == "" or str2 == "":
        if prefix not in list_of_common:
            list_of_common.append(prefix)
        return True
    res1 = find_first_common_letter(str1, str2)
    if res1[2] != "":
        find_next_common(str1[res1[0]+1:], str2[res1[1]+1:], prefix + res1[2], list_of_common)
    else:
        if prefix not in list_of_common:
            list_of_common.append(prefix)
    return True


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
        string1 = get_string_reminder(string1, c)
        string2 = get_string_reminder(string2, c)
        if i == len(result) - 1:
            res1 = "".join([res1, string1[ind1:]])
            res2 = "".join([res2, string2[ind2:]])
    return res1 + '\n' + res2 + '\n' + res + "\n" + 40*"-"+"\n"


def get_string_reminder(string, char):
    ind = string.find(char)
    return string[ind + 1:]


def main():
    # start = time.time()
    with open(sys.argv[1], 'r') as test_cases, open("result.txt", 'w') as result_file:
        for test in test_cases:
            if test[-1] == "\n":
                test = test[:-1]
            if test != "":
                [str1, str2] = test.split(";")
                list_of_new = []
                for i, c1 in enumerate(string1):
                    for n, c2 in enumerate(string2):
                        if c1 == c2:
                            process_strings_from(i, n, string1, string2, result_list)

                # for i, _ in enumerate(str1):
                #     for n, _ in enumerate(str2):
                #         find_next_common(str1[i:], str2[n:], "", list_of_new)
                #         find_next_common(str2[n:], str1[i:], "", list_of_new)

                longest = ""
                for lcs in list_of_new:
                    if len(lcs) > len(longest):
                        longest = lcs
                print "%s:'%s'" % (test, longest.strip())
                result = "%s:'%s'" % (test, longest.strip())
                result = process_line(result)
                result_file.write(result)
    # print time.time() - start

if __name__ == '__main__':
    main()
