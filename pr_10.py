#generate a random number between 1 and 9 , ask the user to guess the number,then tell them whether they guessed too low, too high,or exactly right
import random
random_number = random.randint(1, 9)

guess = int(input("Guess a number between 1 and 9: "))


if guess == random_number:
    print("Congratulations! You guessed the number.")
elif guess < random_number:
    print("Your guess is too low.")
else:
    print("Your guess is too high.")
