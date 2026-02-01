import random

# Number Guessing Game
# ----------------------------------------
# This program generates a random number between 1 and 100.
# The user is given 10 chances to guess the correct number.
# After each guess, the program tells whether the guessed
# number is higher or lower than the actual number.
# If the user guesses the correct number within the given
# chances, they win the game.
# If all chances are used and the number is not guessed,
# the game ends and the correct number is revealed.

random_number = random.randint(1, 100)
chances = 10

while chances > 0:
    try:
        n = int(input("Make a guess (1-100): "))
    except ValueError:
        print("Invalid input! Enter a number.")
        continue

    if n == random_number:
        print("🎉 You won!")
        break
    elif n > random_number:
        chances -= 1
        print(f"Too high! Chances left: {chances}")
    else:
        chances -= 1
        print(f"Too low! Chances left: {chances}")

else:
    print(f"❌ Game over! The number was {random_number}")
