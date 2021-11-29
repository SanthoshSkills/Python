largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        x = int(num)
    except:
        print("Invalid input")
        continue
    if smallest is None:
        smallest = x
        largest = x
    elif x < smallest:
        smallest = x
    elif x > largest:
        largest = x

print("Maximum is", largest)
print("Minimum is", smallest)
