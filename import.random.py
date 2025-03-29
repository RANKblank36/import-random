import random

number = random.randint(1, 100)
while True:
    guess = int(input("Guess the numberv(1-100): "))
    if guess == number:
        print("🎉 Correct! You guessed it.")
        break
    elif guess < number - 20:
        print("Too Lowee!")
    elif guess > number + 20:
        print("Too uper!")
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")