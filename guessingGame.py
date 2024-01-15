import random

randnum = random.randint(1,101)

count  = 0
guess = -1

while (guess != randnum):
    guess = input("Enter your guess between 1 and 100: ")
    guess = int(guess)

    if  guess < randnum:
        print("Your guess is too low")
        count = count + 1
    elif guess > randnum:
        print("Your guess is too high")
        count = count + 1
    else:
        print("You guessed it in ", count, " tries")

