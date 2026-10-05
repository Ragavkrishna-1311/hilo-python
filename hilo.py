import random

number = random.randint(1, 100)
attempts = 0

print("Welcome to the Hi-Lo Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! You got it in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a valid number.")
