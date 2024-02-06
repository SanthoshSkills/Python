import random
n = random.randrange(0,10000)
guess = int(input("Enter any number between 0 and 10000 (both inclusive): "))
while n!= guess:
    if guess < n:
        print("too low")
        guess = int(input("Take another guess: "))
    if guess > n:
        print("too high")
        guess = int(input("Take another guess: "))
    else:
        break
print("you guessed it right")