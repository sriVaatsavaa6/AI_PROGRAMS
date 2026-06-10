import random

n = random.randint(1, 100)
a = 0

print("Welcome to Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.")

while a < 5:
    g = int(input("Guess the number (1 - 100): "))

    if g == n:
        print(f"Congratulations! You guessed the number {n} correctly!")
        break
    elif g < n:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    a += 1

if a == 5 and g != n:
    print(f"Sorry, you've run out of attempts! The correct number was {n}.")
