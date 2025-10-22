print("welcome to Guess the Number!")
print("The rules are simple.I will think of a number,and you will try to guess it .")
import random
number=random.randint(1,10)
IsGuessRight=False
while IsGuessRight!=True:
    guess=input("Guess a number between 1 and 10: ")
    if int(guess)==number:
        print("You guessed {}. That is correct! You win!".format(guess))
        IsGuessRight=True
    else:
        print("You guessed {}.sorry,that isn't it.Try again.".format(guess))