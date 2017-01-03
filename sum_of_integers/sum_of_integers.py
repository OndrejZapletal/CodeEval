import sys

source = []
source.append("-10,2,3,-2,0,5,-15")
source.append("2,3,-2,-1,10")
source.append("-425")
source.append("1,2,3")


def largest_sum(input_list):
    input_list = [int(i) for i in input_list.split(',')]
    largest = sum(input_list)
    for i  in range(len(input_list)):
        for n in range(i,len(input_list)):
            res = sum(input_list[i:n+1])
            if res > largest:
                largest = res
    return largest


for i in source:
    print(largest_sum(i))
