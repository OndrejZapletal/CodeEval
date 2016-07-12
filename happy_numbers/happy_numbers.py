previous_results = []
test = "22"
success = False
while test not in previous_results:
    previous_results.append(test)
    temp_result = 0
    for c in test:
        temp_result = temp_result + int(c) * int(c)
    test = str(temp_result)

    if test == "1":
        success = True
        break
if success:
    print "1"
else:
    print "0"
