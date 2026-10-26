
import random


WORDS = [
    "python",
    "computer",
    "hangman",
    "program",
    "developer",
    "keyboard",
    "internet",
    "science",
    "student",
    "monitor"
]


HANGMAN_STAGES = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]


def display_word(secret_word, guessed_letters):
    """Show guessed letters and hide the remaining letters."""
    return " ".join(
        letter.upper() if letter in guessed_letters else "_"
        for letter in secret_word
    )


def play_hangman():
    """Run one complete Hangman game."""
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = set()
    max_attempts = 6

    print("\nWelcome to Hangman!")
    print("Guess the secret word one letter at a time.")

    while len(wrong_guesses) < max_attempts:
        print(HANGMAN_STAGES[len(wrong_guesses)])
        print("\nWord:", display_word(secret_word, guessed_letters))
        print("Guessed letters:", " ".join(
            sorted(letter.upper() for letter in guessed_letters | wrong_guesses)
        ) or "None")
        print("Attempts remaining:", max_attempts - len(wrong_guesses))

        guess = input("Guess a letter: ").strip().lower()

        
        if len(guess) != 1 or not guess.isalpha() or not guess.isascii():
            print("Please enter a single English letter (A-Z).")
            continue

        
        if guess in guessed_letters or guess in wrong_guesses:
            print("You already guessed that letter. Try another one!")
            continue

        
        if guess in secret_word:
            guessed_letters.add(guess)
            print("Correct guess!")
        else:
            wrong_guesses.add(guess)
            print("Wrong guess!")

        
        if all(letter in guessed_letters for letter in secret_word):
            print("\n" + display_word(secret_word, guessed_letters))
            print("Congratulations! You guessed the word correctly!")
            return

    
    print(HANGMAN_STAGES[max_attempts])
    print("\nGame Over! You ran out of attempts.")
    print("The secret word was:", secret_word.upper())


if __name__ == "__main__":
    play_hangman()


