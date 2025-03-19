import random

def main() -> None:
    # Define a number for player to guess
    number: int = random.randint(0, 100)
    guesser(number)

def guesser(number: int) -> None:
    # Loop for player to keep guessing
    while True:
        # Get players guess
        try:
            guess: int = int(input("Give a number: "))
        except ValueError:
            print("Please enter a number!")
            continue

        # Compare the guess with number
        if guess < number:
            print("Too low. Guess again!")
            continue
        elif guess > number:
            print("Too high. Guess again!")
            continue
        # End the game when the player guesses correctly
        else:
            print("Correct! You win!")
            break

if __name__ == "__main__":
    main()