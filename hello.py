from random import randint


guess = input('Guess a number between 1 and 1000: ')
answer = randint(1,1000)
while guess != answer:
    guess = input('Try Again: ')

print('Correct! ' + guess + ' is the answer!')