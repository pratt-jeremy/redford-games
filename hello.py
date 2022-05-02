from random import randint
from art import *

guesses = 10

print("Guesses Left: " + str(guesses))
guess = int(input('Guess a number between 1 and 100: '))
answer = randint(1,100)
while guess != answer:
    if guesses == 0:
        print("YOU FAILED!!")
        print("The Answer Was: " + str(answer))
        print(art("angry"))
    else:
        guesses = guesses - 1
        if guess > answer:
            print("Guesses Left: " + str(guesses))
            print(art("cat"))
            guess = int(input('Too High: '))
        if guess < answer:
            print("Guesses Left: " + str(guesses))
            print(art("sad"))
            guess = int(input('Too Low: '))

print(art("happy"))
print('Correct! ' + str(guess) + ' is the answer!')