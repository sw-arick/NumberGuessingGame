import random

attempts = 7

def displayRules():
    print("Welcome to Number Guessing Game!\n")
    print("I have selected a number between 1 and 100.")
    print("You have 7 attempts to guess it.\n")

def playGame(number, attempt=1):
    if attempt > attempts:
        print("\nGame Over!")
        print("The correct number was:", number)
        return

    guess = input(f"Attempt {attempt}/7 - Enter your guess: ")

    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.\n")
        return playGame(number, attempt)

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.\n")
        return playGame(number, attempt)

    checkGuess = lambda x,y: "correct" if x == y else (
        "low" if x < y else "high"
    )

    result = checkGuess(guess, number)

    if result == "correct":
        print("\nCongratulations! You guessed the correct number!")
        print("You guessed it in", attempt, "attempt(s).")
        return

    if result == "low":
        print("Too Low! Try a higher number.\n")
    else :
        print("Too High! Try a lower number.\n")

    playGame(number, attempt+1)


displayRules()
random_number = random.randint(1, 100)
playGame(random_number)