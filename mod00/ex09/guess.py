import sys
import random
import signal

def handle_exit(sig, frame):
    """Handles Ctrl+C and SIGTERM for a clean exit."""
    print("\nGame interrupted. Exiting safely. Goodbye!")
    sys.exit(0)

# Catch Ctrl+C (SIGINT) and system kill (SIGTERM)
signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)

def guess_game():
    to_guess = random.randint(1, 99)
    guess_count = 0
    while True:
        try:
            guess = int(input("What's your guess between 1 and 99?\n"))
        except ValueError:
            print("That's not a number.")
            continue
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting safely.")
            sys.exit(0)

        guess_count += 1

        if guess == to_guess:
            if guess_count == 42:
                print("I see you brought your towel with you!", end="")
            if guess_count == 0:
                print("Congratulations! You got it on your first try!", end="")
                return
            else:
                print(f"That's it! Congratulations!\nYou won in {guess_count}", end="")
                return
        elif guess < to_guess:
            print("Too low!")
        elif guess > to_guess:
            print("Too high!")

guess_game()