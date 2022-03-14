import random

number = random.randint(0,10)
guess = int(input("I'm thinking of a number. betwwen 0 and 10. I can guess it:"))

while True:
    if number == guess:
        break
    else:
        guess = int(input("Nope. I guess again:"))
print('You guessed right. I was thinking about',guess)