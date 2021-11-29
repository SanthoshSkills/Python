import re
#handle = open('regex_sum_42.txt')
handle = open('regex_sum_1418674.txt')
numbers = list()
for line in handle :
    stuff = re.findall('[0-9]+', line)
    if len(stuff) > 0:
        for x in range(len(stuff)) :
            num = int(stuff[x])
            numbers.append(num)
print("There are",len(numbers),"values with a sum =", sum(numbers))
