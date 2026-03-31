import random
import os

# Hangman stages (ASCII art)
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

# List of words with hints
WORDS_WITH_HINTS = [
    ("python", "A programming language"),
    ("hangman", "The name of this game"),
    ("computer", "An electronic device"),
    ("algorithm", "A set of rules to solve a problem"),
    ("developer", "Someone who writes code"),
    ("keyboard", "Input device for computers"),
    ("monitor", "Display device"),
    ("internet", "Global network of computers"),
    ("software", "Programs and applications"),
    ("database", "Organized collection of data")
]

def get_random_word():
    """Get a random word and its hint."""
    return random.choice(WORDS_WITH_HINTS)

def display_game_state(word_progress, guessed_letters, wrong_guesses, hint):
    """Display the current game state."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    print("Welcome to Hangman!")
    print(HANGMAN_STAGES[wrong_guesses])
    print(f"Word: {' '.join(word_progress)}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print(f"Wrong guesses: {wrong_guesses}/6")
    print(f"Hint: {hint}")
    print()

def play_hangman():
    """Main game function."""
    word, hint = get_random_word()
    word_progress = ['_'] * len(word)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    while wrong_guesses < max_wrong and '_' in word_progress:
        display_game_state(word_progress, guessed_letters, wrong_guesses, hint)
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            input("Press Enter to continue...")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            input("Press Enter to continue...")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    word_progress[i] = guess
            print("Good guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

        input("Press Enter to continue...")

    display_game_state(word_progress, guessed_letters, wrong_guesses, hint)

    if '_' not in word_progress:
        print("Congratulations! You won!")
    else:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    play_hangman()