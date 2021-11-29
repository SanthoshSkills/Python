score = input("Enter Score: ")
try:
    s = float(score)
except:
    print('Please enter a number')
    quit()
print(s)
if s < 0.0 or s > 1.0:
    print('Number entered is out of range, ensure it is between 0 and 1')
    quit()
elif s < 0.6:
    print("F")
elif s < 0.7:
    print("D")
elif s < 0.8:
    print("C")
elif s < 0.9:
    print("B")
else: print("A")
