import random

# Task 1 - Create the entry file and print welcome message
# Step 1: Entry File Setup
# Step 2: Welcome Banner Output
def print_welcome():
    print("Welcome to Hangman!")


# Task 2 - Define word pool, maximum lives, and gallows stages
# Step 1: Declare Secret Word Pool
WORDS = ["PYTHON", "PLANET", "ROBOT", "GUITAR", "SILVER", "ROCKET", "CODING"]

# Step 2: Declare Maximum Lives Threshold
MAX_LIVES = 6

# Step 3: Declare Gallows ASCII Art Stages
STAGES = [
    # 0 mistakes (6 lives left)
    """  +---+
  |   |
      |
      |
      |
      |
=========""",
    # 1 mistake (5 lives left)
    """  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    # 2 mistakes (4 lives left)
    """  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    # 3 mistakes (3 lives left)
    """  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    # 4 mistakes (2 lives left)
    """  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    # 5 mistakes (1 life left)
    """  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    # 6 mistakes (0 lives left - Game Over)
    """  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========="""
]


# Task 3 - Build the masked word string
# Step 1: Initialize Masked Character Collection
# Step 2: Iterate Letters and Reveal Guessed Characters
# Step 3: Join and Return Formatted Masked String
def get_masked_word(secret_word, guessed_letters):
    display_chars = []
    for letter in secret_word:
        if letter in guessed_letters:
            display_chars.append(letter)
        else:
            display_chars.append("_")
    return " ".join(display_chars)


# Task 4 - Check word completion status
# Step 1: Scan Secret Word for Unsolved Letters
# Step 2: Return Boolean Guess Status
def is_word_guessed(secret_word, guessed_letters):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


# Task 5 - Format guessed letters display
# Step 1: Sort Guessed Letters Alphabetically
# Step 2: Construct Comma-Separated Guessed Letters String
def format_guessed_letters(guessed_letters):
    if not guessed_letters:
        return "None"
    sorted_letters = sorted(list(guessed_letters))
    return ", ".join(sorted_letters)


# Task 6 - Render gallows and full game board
# Step 1: Print Gallows ASCII Stage for Current Mistake Count
# Step 2: Print Masked Word Display
# Step 3: Print Formatted Guessed Letters
# Step 4: Print Remaining Lives Tally
def display_board(wrong_guesses, secret_word, guessed_letters):
    print("\n" + STAGES[wrong_guesses])
    print(f"\nWord: {get_masked_word(secret_word, guessed_letters)}")
    print(f"Guessed letters: {format_guessed_letters(guessed_letters)}")
    lives_left = MAX_LIVES - wrong_guesses
    print(f"Lives remaining: {lives_left} / {MAX_LIVES}")


# Task 7 - Read and normalize letter input
# Step 1: Prompt Player for Guess Input
# Step 2: Trim Whitespace and Convert to Uppercase
def read_raw_guess():
    raw_text = input("\nEnter your guess (a single letter): ")
    return raw_text.strip().upper()


# Task 8 - Validate character format
# Step 1: Verify Exactly One Character Length
# Step 2: Verify Character is Alphabetic
def is_valid_format(guess):
    return len(guess) == 1 and guess.isalpha()


# Task 9 - Check duplicates and finalize guess input
# Step 1: Verify Letter Has Not Been Guessed Yet
# Step 2: Output Friendly Duplicate Notification
# Step 3: Loop Until Valid Unique Letter Received
def get_valid_guess(guessed_letters):
    while True:
        guess = read_raw_guess()
        if not is_valid_format(guess):
            print("Invalid input. Please enter exactly one alphabetic letter (A-Z).")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
        else:
            return guess


# Task 10 - Create the Hangman class constructor
class Hangman:
    def __init__(self):
        # Step 1: Initialize Secret Word Attribute
        self.secret_word = ""
        # Step 2: Initialize Guessed Letters Collection Attribute
        self.guessed_letters = []
        # Step 3: Initialize Wrong Guesses Counter Attribute
        self.wrong_guesses = 0

    # Task 11 - Implement word selection and game reset
    def reset_game(self):
        # Step 1: Pick Random Word from Word Pool
        self.secret_word = random.choice(WORDS)
        # Step 2: Reset Guessed Letters Collection
        self.guessed_letters = []
        # Step 3: Reset Wrong Guesses Counter to Zero
        self.wrong_guesses = 0

    # Task 12 - Implement single guess processing
    def process_guess(self, letter):
        # Step 1: Register Letter in Guessed Letters Collection
        self.guessed_letters.append(letter)
        # Step 2: Branch on Match: Announce Correct Guess
        if letter in self.secret_word:
            print(f"\nGood guess! '{letter}' is in the word!")
        # Step 3: Branch on Miss: Increment Wrong Guesses and Announce Miss
        else:
            self.wrong_guesses += 1
            print(f"\nSorry! '{letter}' is not in the word.")

    # Task 13 - Announce outcome and reveal secret word
    def announce_result(self):
        # Step 1: Render Final Game Board State
        display_board(self.wrong_guesses, self.secret_word, self.guessed_letters)
        # Step 2: Evaluate Victory Condition and Congratulate Player
        if is_word_guessed(self.secret_word, self.guessed_letters):
            print(f"\nCONGRATULATIONS! You solved the secret word: {self.secret_word}!")
        # Step 3: Evaluate Defeat Condition and Reveal Secret Word
        else:
            print(f"\nGAME OVER! You ran out of lives. The secret word was: {self.secret_word}.")

    # Task 14 - Construct single-game turn loop
    def play_round(self):
        # Step 1: Reset Game State for New Match
        self.reset_game()
        # Step 2: Print Match Start Banner
        print("\n===== NEW HANGMAN GAME =====")
        print(f"A secret word has been chosen with {len(self.secret_word)} letters. Good luck!")

        # Step 3: Run Turn Loop While Alive and Unsolved
        while self.wrong_guesses < MAX_LIVES and not is_word_guessed(self.secret_word, self.guessed_letters):
            display_board(self.wrong_guesses, self.secret_word, self.guessed_letters)
            guess = get_valid_guess(self.guessed_letters)
            self.process_guess(guess)

        # Step 4: Call Outcome Announcer
        self.announce_result()

    # Task 15 - Implement rematch prompt
    @staticmethod
    def ask_replay():
        # Step 1: Run Interactive Replay Prompt Loop
        while True:
            # Step 2: Read and Normalize Confirmation Input
            answer = input("\nPlay again? (y/n): ").strip().lower()
            # Step 3: Return Boolean Replay Decision
            if answer == "y":
                return True
            elif answer == "n":
                return False
            print("Please type y or n.")

    # Task 16 - Construct multi-game session loop
    def play_many(self):
        # Step 1: Run Indefinite Session Loop
        while True:
            # Step 2: Execute Game Lifecycle
            self.play_round()
            # Step 3: Prompt for Rematch Confirmation
            if not self.ask_replay():
                # Step 4: Print Session Farewell on Exit
                print("\nThanks for playing Hangman!")
                break


# Task 17 - Assemble the main() entry point
def main():
    # Step 1: Call Welcome Banner Function
    print_welcome()
    # Step 2: Instantiate Hangman Game Manager
    game = Hangman()
    # Step 3: Launch Multi-Game Session Loop
    game.play_many()


if __name__ == "__main__":
    main()
