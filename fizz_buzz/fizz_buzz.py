import sys

with open(sys.argv[1], 'r') as test_case:
    for test in test_case:
        if test[-1] == '\n':
            test = test[:-1]
        if test:
            [fizz, buzz, count] = test.split()
            ret_val = ""
            for i in range(1, int(count) + 1):
                if not (i % int(fizz) or i % int(buzz)):
                    ret_val += "FB "
                elif not (i % int(fizz)):
                    ret_val += "F "
                elif not (i % int(buzz)):
                    ret_val += "B "
                else:
                    ret_val += str(i) + " "
            print("%s" % ret_val[:-1])
