import random

num = random.randint(1, 20)

attempt = 0

guess = 0

while guess != num:
    guess = eval(input("Guess the number: "))
    attempt += 1


    if guess > num:
        print("Too high!")
    elif guess < num:
        print("Too low!")
print("Guessed in ", attempt, " attempts")