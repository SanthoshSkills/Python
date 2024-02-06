#mean
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
mean = sum(list1) / len(list1)
print("Mean: ",mean)

#median
list1.sort()
if len(list1) %2 == 0:
    m1 = list1[len(list1)//2]
    m2 = list1[len(list1)//2 -1]
    median = m1+m2
else:
    median = list1[len(list1)//2]
print("Median: ",median)

#mode
frequency = {}
for i in list1:
    frequency.setdefault(i,0)
    frequency[i] += 1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i

print("Mode: ",mode)