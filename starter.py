import random
secret_number = random.randint(1,10)
guess = int(input("guess a number between 1 to 10:"))
if guess == secret_number:
    print("U guessed it!")
else:
    print("Better luck next time!")
    