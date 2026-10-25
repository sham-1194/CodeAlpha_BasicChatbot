
import random

def play_hangman():
    words = ["python", "computer", "program", "developer", "keyboard"]
    secret_word = random.choice(words)
    guessed_letters = set()
    attempts = 6

    print("\n=== CODEALPHA HANGMAN GAME ===")
    print("Guess the word one letter at a time!")
    print("You have", attempts, "wrong guesses allowed.")

    while attempts > 0:
        display_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )
        print("\nWord:", display_word)
        print("Wrong guesses left:", attempts)

        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You guessed the word:", secret_word)
            break

        guess = input("Enter a letter (or 'quit' to exit): ").lower().strip()

        if guess == "quit":
            print("Game ended. The word was:", secret_word)
            break

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter only.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            attempts -= 1
            print("Wrong guess!")

    else:
        print("\nGame over! The word was:", secret_word)


if __name__ == "__main__":
    play_hangman()
