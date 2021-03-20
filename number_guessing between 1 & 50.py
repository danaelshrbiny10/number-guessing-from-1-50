import random

number = random. randrange(1,50)
guess = int(input("guess a number between 1 and 50: "))

while guess != number:
    if guess < number:
        print("you need to guess higher , try again!")
        guess = int(input("\n guess a number between 1 and 50: "))
    else:
        print("you need to guess lower , try again!")
        guess = int(input("\n guess a number between 1 and 50: "))

print("you guessed the number correctly ...!")