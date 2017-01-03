import sys

source = []
source.append("2")
source.append("0")
source.append("10")
source.append("67")
source.append("33")


def to_binary(string):
    number = int(string)
    reminder_result = ""
    reminder = 0
    while number > 0:
        reminder = int(number % 2)
        reminder_result = str(reminder) + reminder_result
        number = int((number - reminder) / 2)
    if reminder_result != "":
        return reminder_result
    else:
        return "0"


for i in source:
    print(to_binary(i))
