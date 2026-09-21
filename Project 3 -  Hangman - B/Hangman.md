<u>**PROJECT 3 (Beginner)**</u>

# Hangman Word Guessing Game

Build an interactive, beginner-friendly Hangman word guessing game: model game state with object-oriented design, implement string masking and character verification logic, render progressive multi-stage ASCII gallows visual art, manage lives deduction and win/loss resolution, and support continuous session replay in a clean command-line interface. Language-agnostic — code it in **Python**, **C++**, or **Java**.

---

### Curriculum Outline & Learning Roadmap

- **Chapter 1: Introduction**

  - `1.1 Getting Started`

    - `[CONCEPT]` Meet Your Project

    - `[CONCEPT]` What You Will Learn

    - `[CONCEPT]` What You Need

  - `1.2 Starting with Small Steps`

    - `[CONCEPT]` First Steps into Code: The Welcome Banner

    - `[TASK 1]` Create the entry file and print welcome message

    - `[CHECKPOINT]` Milestone Checkpoint: Welcome Banner Functional!

    - `[CONCEPT]` Secret Word Pool & Lives Boundary

    - `[TASK 2]` Define word pool, maximum lives, and gallows stages

    - `[CHECKPOINT]` Milestone Checkpoint: Game Configuration Defined!

- **Chapter 2: Specifications & Architectural Plan**

  - `2.1 Understanding the Domain & Rules`

    - `[CONCEPT]` Core Rules & Multi-Stage Gallows Mechanics

    - `[CONCEPT]` Character Masking & Reveal Pipeline

  - `2.2 Chronological Execution Flow`

    - `[CONCEPT]` Chronological Execution Flow (5 Stages)

  - `2.3 System Architecture: Thinking in OOP`

    - `[CONCEPT]` Thinking in OOP (Component Responsibility Table)

- **Chapter 3: Core Word Masking Logic**

  - `3.1 Word Masking Pipeline`

    - `[CONCEPT]` Masked String Generation

    - `[TASK 3]` Build the masked word string

    - `[CHECKPOINT]` Milestone Checkpoint: Masked Word Generator Operational!

  - `3.2 Win Condition Evaluation`

    - `[CONCEPT]` Word Completion Scan

    - `[TASK 4]` Check word completion status

    - `[CHECKPOINT]` Milestone Checkpoint: Win Condition Logic Verified!

- **Chapter 4: Visual Board & Defensive Input Pipeline**

  - `4.1 Formatted Board Rendering`

    - `[CONCEPT]` Alphabetical Guessed Letters

    - `[TASK 5]` Format guessed letters display

    - `[CHECKPOINT]` Milestone Checkpoint: Guessed Letters Formatter Functional!

    - `[CONCEPT]` ASCII Gallows Visualization

    - `[TASK 6]` Render gallows and full game board

    - `[CHECKPOINT]` Milestone Checkpoint: Visual Board Display Operational!

  - `4.2 Defensive Input Validation Engine`

    - `[CONCEPT]` Raw Input Capture & Normalization

    - `[TASK 7]` Read and normalize letter input

    - `[CHECKPOINT]` Milestone Checkpoint: Raw Input Capture Operational!

    - `[CONCEPT]` Character Format Validation

    - `[TASK 8]` Validate character format

    - `[CHECKPOINT]` Milestone Checkpoint: Character Format Validation Functional!

    - `[CONCEPT]` Duplicate Prevention & Re-prompt Loop

    - `[TASK 9]` Check duplicates and finalize guess input

    - `[CHECKPOINT]` Milestone Checkpoint: Defensive Guess Pipeline Complete!

- **Chapter 5: Building the Game Engine (Thinking in OOP)**

  - `5.1 Game State & Reset Mechanics`

    - `[CONCEPT]` State Encapsulation in Hangman Class

    - `[TASK 10]` Create the Hangman class constructor

    - `[CHECKPOINT]` Milestone Checkpoint: Hangman State Initialized!

    - `[CONCEPT]` Secret Word Selection & Fresh State Initialization

    - `[TASK 11]` Implement word selection and game reset

    - `[CHECKPOINT]` Milestone Checkpoint: Game Reset & Word Selection Operational!

  - `5.2 Guess Processing & Outcome Resolution`

    - `[CONCEPT]` Registering Letters & Decrementing Lives

    - `[TASK 12]` Implement single guess processing

    - `[CHECKPOINT]` Milestone Checkpoint: Guess Processing & Lives Deduction Verified!

    - `[CONCEPT]` Result Announcement & Secret Reveal

    - `[TASK 13]` Announce outcome and reveal secret word

    - `[CHECKPOINT]` Milestone Checkpoint: Game Outcome Presentation Operational!

  - `5.3 Single-Game Turn Loop`

    - `[CONCEPT]` Turn-Based Lifecycle Architecture

    - `[TASK 14]` Construct single-game turn loop

    - `[CHECKPOINT]` Milestone Checkpoint: Single-Game Turn Loop Complete!

- **Chapter 6: Adding Replayability & Full Application Execution**

  - `6.1 Session Management`

    - `[CONCEPT]` Interactive Rematch Confirmation

    - `[TASK 15]` Implement rematch prompt

    - `[CHECKPOINT]` Milestone Checkpoint: Rematch Prompt Functional!

    - `[CONCEPT]` Multi-Game Continuous Session Engine

    - `[TASK 16]` Construct multi-game session loop

    - `[CHECKPOINT]` Milestone Checkpoint: Multi-Game Session Engine Complete!

  - `6.2 Application Assembly`

    - `[CONCEPT]` Program Inception & Launch Pipeline

    - `[TASK 17]` Assemble the main() entry point

    - `[CHECKPOINT]` Milestone Checkpoint: Full Application Experience Achieved!

- **Chapter 7: Reflect & Expand**

  - `7.1 What You Have Built` (Feature Summary & Skills Practiced Matrix)

  - `7.2 Extension Ideas`

  - `7.3 Share What You Built! Time to Showcase Your Project!`

- **Appendix: Full Pseudocode Reference**

  - `[REFERENCE]` Complete Tri-Language Algorithmic Logic

---

## Chapter 1: Introduction

### 1.1 Getting Started

**Meet Your Project**

You are about to build **Hangman** — the classic word-guessing puzzle — as a fully functional, interactive terminal game. In this project, a secret word is selected at random from an approved vocabulary bank, and the player attempts to decipher it one letter at a time before running out of attempts.

This project reinforces essential software development patterns: string manipulation, character iteration, state tracking, defensive CLI input parsing, procedural-to-object-oriented architecture transitions, and terminal visualization with ASCII art.

By completing this workbook, you will gain hands-on mastery over stateful game loops, collection filtering, input sanitation, and class construction in **Python**, **C++**, or **Java**.

**What You Will Learn**

Throughout this guided curriculum, you will build this application step by step. By the end, you will have a complete, production-grade project you can execute, explain, and expand.

You will learn how to:

1. Maintain immutable word collections and configuration constants without magic numbers
2. Dynamically mask and unmask secret strings based on player guess histories
3. Validate user inputs defensively against invalid character counts, non-alphabetic inputs, and duplicate guesses
4. Render multi-stage ASCII gallows visual art corresponding precisely to the remaining lives count
5. Encapsulate mutable round data inside an object-oriented `Hangman` class
6. Drive a turn-based execution loop that alternates between state updates and screen presentations
7. Handle end-of-game victory and defeat conditions gracefully with informative feedback
8. Implement an interactive rematch confirmation cycle that allows players to enjoy continuous gaming sessions

**What You Need**

Before you begin, ensure you have basic familiarity with:

- Terminal input and output (`input()` / `print()` in Python, `cin` / `cout` in C++, `Scanner` / `System.out.println()` in Java)
- Primitive data types, strings, lists/vectors, and arrays
- Conditional decision making (`if` / `else`) and loops (`while`, `for`)
- Basic class declarations and instance methods

---

### 1.2 Starting with Small Steps

**First Steps into Code: The Welcome Banner**

Every well-engineered application starts with a clean greeting that informs the player what software has launched. We begin by creating our project entry file and defining our banner printer.

#### Task 1 — Create the entry file and print welcome message

Establish the application entry file and output the initial greeting banner:

Think of the opening curtain of a theater stage before the actors emerge.  
*Goal*: Print the official game title to the terminal standard output.

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 1</span>
    <span class="step-title">Entry File Setup</span>
  </div>
  <ul>
    <li>[ ] Create your project source file (<code>Hangman.py</code>, <code>Hangman.cpp</code>, or <code>Hangman.java</code>).</li>
    <li>[ ] Include required foundational standard libraries and establish the primary module namespace.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 2</span>
    <span class="step-title">Welcome Banner Output</span>
  </div>
  <ul>
    <li>[ ] Define a function or method named <code>print_welcome()</code> (or <code>printWelcome()</code>).</li>
    <li>[ ] Print the text <code>"Welcome to Hangman!"</code> followed by a newline.</li>
  </ul>
</div>

<div class="lang-tab python"><span class="lang-dot"></span>Python</div>

```python
# Task 1 - Create the entry file and print welcome message
# Step 1: Entry File Setup
# Step 2: Welcome Banner Output
def print_welcome():
    print("Welcome to Hangman!")
```

<div class="lang-tab cpp"><span class="lang-dot"></span>C++</div>

```cpp
// Task 1 - Create the entry file and print welcome message
// Step 1: Entry File Setup
// Step 2: Welcome Banner Output
void printWelcome() {
    cout << "Welcome to Hangman!\n";
}
```

<div class="lang-tab java"><span class="lang-dot"></span>Java</div>

```java
// Task 1 - Create the entry file and print welcome message
// Step 1: Entry File Setup
// Step 2: Welcome Banner Output
public static void printWelcome() {
    System.out.println("Welcome to Hangman!");
}
```

### Milestone Checkpoint: Welcome Banner Functional!

You have established the entry point of your application:

- [x] **Source File Established**: Created clean project file with required system imports.
- [x] **Banner Output Operational**: Greeting function cleanly outputs the game title.

**Driver Verification Test**:  
Execute `print_welcome()` (or `printWelcome()`). Verify that `Welcome to Hangman!` prints cleanly to the console.

---

**Secret Word Pool & Lives Boundary**

Hangman requires an approved vocabulary list from which mystery words are picked, an integer defining how many incorrect guesses are allowed before defeat, and graphical representations for each mistake stage.

#### Task 2 — Define word pool, maximum lives, and gallows stages

Define the immutable word list, lives limit, and ASCII gallows illustrations:

Think of loading the game cartridge with puzzle words, drawing 6 empty hearts on the health bar, and sketching the stages of the gallows.  
*Goal*: Provide constant data collections that govern game difficulty and visuals.

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 1</span>
    <span class="step-title">Declare Secret Word Pool</span>
  </div>
  <ul>
    <li>[ ] Declare a constant list or array named <code>WORDS</code> populated with uppercase words: <code>"PYTHON"</code>, <code>"PLANET"</code>, <code>"ROBOT"</code>, <code>"GUITAR"</code>, <code>"SILVER"</code>, <code>"ROCKET"</code>, <code>"CODING"</code>.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 2</span>
    <span class="step-title">Declare Maximum Lives Threshold</span>
  </div>
  <ul>
    <li>[ ] Declare an integer constant named <code>MAX_LIVES</code> set to <code>6</code>.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 3</span>
    <span class="step-title">Declare Gallows ASCII Art Stages</span>
  </div>
  <ul>
    <li>[ ] Declare a list or array named <code>STAGES</code> containing 7 multiline ASCII strings representing mistake counts from 0 (empty gallows) up to 6 (full figure / Game Over).</li>
  </ul>
</div>

<div class="lang-tab python"><span class="lang-dot"></span>Python</div>

```python
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
```

<div class="lang-tab cpp"><span class="lang-dot"></span>C++</div>

```cpp
// Task 2 - Define word pool, maximum lives, and gallows stages
// Step 1: Declare Secret Word Pool
const vector<string> WORDS = {"PYTHON", "PLANET", "ROBOT", "GUITAR", "SILVER", "ROCKET", "CODING"};

// Step 2: Declare Maximum Lives Threshold
const int MAX_LIVES = 6;

// Step 3: Declare Gallows ASCII Art Stages
const vector<string> STAGES = {
    "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
};
```

<div class="lang-tab java"><span class="lang-dot"></span>Java</div>

```java
// Task 2 - Define word pool, maximum lives, and gallows stages
// Step 1: Declare Secret Word Pool
static final String[] WORDS = {"PYTHON", "PLANET", "ROBOT", "GUITAR", "SILVER", "ROCKET", "CODING"};

// Step 2: Declare Maximum Lives Threshold
static final int MAX_LIVES = 6;

// Step 3: Declare Gallows ASCII Art Stages
static final String[] STAGES = {
    "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
};
```

### Milestone Checkpoint: Game Configuration Defined!

You have established the core parameters of the game:

- [x] **Word Pool Established**: 7 distinct uppercase words configured.
- [x] **Lives Limit Fixed**: `MAX_LIVES = 6` without magic numbers.
- [x] **Gallows Art Configured**: 7 progressive visual stages indexed by mistake count.

**Driver Verification Test**:  
Print `len(WORDS)` (or `WORDS.size()` / `WORDS.length`) and verify it equals `7`. Print `len(STAGES)` and verify it equals `7`. Print `MAX_LIVES` and verify it equals `6`.

---

## Chapter 2: Specifications & Architectural Plan

### 2.1 Understanding the Domain & Rules

**Core Rules & Multi-Stage Gallows Mechanics**

Hangman is played between a single player and the computer. In each round, the computer chooses a secret word from `WORDS`, and the player attempts to uncover all letters of the secret word before making 6 incorrect guesses.

The rules and visual states are governed by mistake counts:

| Mistakes | Lives Remaining | Visual Figure Description | Game State |
|---|---|---|---|
| **0** | 6 | Empty gallows beam and rope | Active Play (Fresh Round) |
| **1** | 5 | Head (`O`) attached to rope | Active Play |
| **2** | 4 | Torso (`|`) drawn | Active Play |
| **3** | 3 | Left arm (`/`) drawn | Active Play |
| **4** | 2 | Right arm (`\`) drawn | Active Play |
| **5** | 1 | Left leg (`/`) drawn | Danger: Final Life! |
| **6** | 0 | Right leg (`\`) drawn | Defeat (Game Over) |

**Character Masking & Reveal Pipeline**

At any point in the game, the word is displayed with known letters revealed and unsolved letters hidden as underscores (`_`). Each character is separated by a single space for clear readability:

![Masking Evaluation Logic](diagram_masking_logic.png)

1. For each character in the secret word, check if it exists in the player's guessed letters list.
2. If the character has been guessed, keep the letter visible.
3. If the character has not been guessed yet, replace it with an underscore (`_`).
4. Join the resulting characters with single space delimiters (e.g., `"P _ _ _ E _"` for `"PLANET"` with guesses `['P', 'E']`).

---

### 2.2 Chronological Execution Flow

**Five-Stage Match Execution Lifecycle**

A complete application session proceeds through five distinct stages:

![Chronological Match Execution Flow](diagram_match_flow.png)

1. **System Inception & Greeting**: Launch the program, display the executive welcome banner, and establish game constants.
2. **Game State Initialization**: Pick a random secret word, initialize the guessed letters collection to empty, and set wrong guesses to 0.
3. **Turn-Based Board & Input Loop**: Render the current gallows ASCII art, display the masked word, show previous guesses and lives remaining, prompt for a single letter, validate input, and record the guess.
4. **Outcome Evaluation**: Verify if all letters in the secret word have been solved (Victory) or if the player has accumulated 6 mistakes (Defeat).
5. **Outcome Announcement & Replay**: Announce congratulations or reveal the secret word, prompt for rematch confirmation, and restart or exit cleanly.

---

### 2.3 System Architecture: Thinking in OOP

**Component Responsibilities & Class Hierarchy**

Separating the game into helper functions and a stateful `Hangman` class isolates data, simplifies debugging, and enables multi-game sessions:

![OOP Class Hierarchy](diagram_oop_class.png)

| Component | Responsibility |
|---|---|
| **HangmanHelperFunctions** | Houses pure static utilities and constants: `WORDS`, `MAX_LIVES`, `STAGES`, `getMaskedWord()`, `isWordGuessed()`, `formatGuessedLetters()`, `displayBoard()`, and `getValidGuess()`. |
| **Hangman** | Holds mutable round state (`secretWord`, `guessedLetters`, `wrongGuesses`). Manages word randomization, single-guess processing, outcome evaluation, turn loops, and replay flow. |
| **MainProgram** | Serves as the program entry point: displays the welcome banner, instantiates the `Hangman` engine, and starts the session loop. |

---

## Chapter 3: Core Word Masking Logic

### 3.1 Word Masking Pipeline

**Masked String Generation**

In Hangman, the player must never see the full secret word until they have correctly guessed its letters. We need a function that takes the `secret_word` and the collection of `guessed_letters`, and outputs a spaced masked string.

#### Task 3 — Build the masked word string

Construct the formatted string displaying guessed letters and underscores:

Think of a word puzzle board where solved letters are flipped over while mystery letters remain face-down tiles.  
*Goal*: Generate a user-facing masked representation like `"P _ _ _ E _"`.

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 1</span>
    <span class="step-title">Initialize Masked Character Collection</span>
  </div>
  <ul>
    <li>[ ] Initialize an empty collection or accumulator named <code>display_chars</code> (or <code>masked</code>).</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 2</span>
    <span class="step-title">Iterate Letters and Reveal Guessed Characters</span>
  </div>
  <ul>
    <li>[ ] Iterate through every character in <code>secret_word</code>.</li>
    <li>[ ] If the character exists in <code>guessed_letters</code>, append the character; otherwise, append an underscore (<code>"_"</code>).</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 3</span>
    <span class="step-title">Join and Return Formatted Masked String</span>
  </div>
  <ul>
    <li>[ ] Combine characters with space delimiters and return the final string.</li>
  </ul>
</div>

<div class="lang-tab python"><span class="lang-dot"></span>Python</div>

```python
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
```

<div class="lang-tab cpp"><span class="lang-dot"></span>C++</div>

```cpp
// Task 3 - Build the masked word string
// Step 1: Initialize Masked Character Collection
// Step 2: Iterate Letters and Reveal Guessed Characters
// Step 3: Join and Return Formatted Masked String
string getMaskedWord(const string& secretWord, const vector<char>& guessedLetters) {
    string masked = "";
    for (size_t i = 0; i < secretWord.size(); ++i) {
        char c = secretWord[i];
        bool found = false;
        for (char g : guessedLetters) {
            if (g == c) {
                found = true;
                break;
            }
        }
        if (found) {
            masked += c;
        } else {
            masked += "_";
        }
        if (i + 1 < secretWord.size()) {
            masked += " ";
        }
    }
    return masked;
}
```

<div class="lang-tab java"><span class="lang-dot"></span>Java</div>

```java
// Task 3 - Build the masked word string
// Step 1: Initialize Masked Character Collection
// Step 2: Iterate Letters and Reveal Guessed Characters
// Step 3: Join and Return Formatted Masked String
public static String getMaskedWord(String secretWord, List<Character> guessedLetters) {
    StringBuilder masked = new StringBuilder();
    for (int i = 0; i < secretWord.length(); i++) {
        char c = secretWord.charAt(i);
        if (guessedLetters.contains(c)) {
            masked.append(c);
        } else {
            masked.append("_");
        }
        if (i + 1 < secretWord.length()) {
            masked.append(" ");
        }
    }
    return masked.toString();
}
```

### Milestone Checkpoint: Masked Word Generator Operational!

You have implemented dynamic word masking:

- [x] **Character Inspection**: Accurately matches guessed characters against target secret letters.
- [x] **Visual Masking**: Replaces unrevealed letters with underscores separated by spaces.

**Driver Verification Test**:  
Execute `get_masked_word("PLANET", ['P', 'E'])`. Verify that the return value is `"P _ _ _ E _"`.

---

### 3.2 Win Condition Evaluation

**Word Completion Scan**

To determine if the player has won the game, we must verify whether every character in the secret word has been guessed. If even a single letter remains unsolved, the game has not been won.

#### Task 4 — Check word completion status

Verify if all letters of the secret word are present in the guessed letters set:

Think of checking if every blank on an answer sheet has been filled in with a correct answer.  
*Goal*: Return `True` if the player has completely solved the secret word, `False` otherwise.

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 1</span>
    <span class="step-title">Scan Secret Word for Unsolved Letters</span>
  </div>
  <ul>
    <li>[ ] Iterate through each character in <code>secret_word</code>.</li>
    <li>[ ] If any character is not found in <code>guessed_letters</code>, immediately return <code>False</code>.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 2</span>
    <span class="step-title">Return Boolean Guess Status</span>
  </div>
  <ul>
    <li>[ ] If the loop completes without finding any missing letters, return <code>True</code>.</li>
  </ul>
</div>

<div class="lang-tab python"><span class="lang-dot"></span>Python</div>

```python
# Task 4 - Check word completion status
# Step 1: Scan Secret Word for Unsolved Letters
# Step 2: Return Boolean Guess Status
def is_word_guessed(secret_word, guessed_letters):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True
```

<div class="lang-tab cpp"><span class="lang-dot"></span>C++</div>

```cpp
// Task 4 - Check word completion status
// Step 1: Scan Secret Word for Unsolved Letters
// Step 2: Return Boolean Guess Status
bool isWordGuessed(const string& secretWord, const vector<char>& guessedLetters) {
    for (char c : secretWord) {
        bool found = false;
        for (char g : guessedLetters) {
            if (g == c) {
                found = true;
                break;
            }
        }
        if (!found) {
            return false;
        }
    }
    return true;
}
```

<div class="lang-tab java"><span class="lang-dot"></span>Java</div>

```java
// Task 4 - Check word completion status
// Step 1: Scan Secret Word for Unsolved Letters
// Step 2: Return Boolean Guess Status
public static boolean isWordGuessed(String secretWord, List<Character> guessedLetters) {
    for (int i = 0; i < secretWord.length(); i++) {
        char c = secretWord.charAt(i);
        if (!guessedLetters.contains(c)) {
            return false;
        }
    }
    return true;
}
```

### Milestone Checkpoint: Win Condition Logic Verified!

You have implemented the game completion check:

- [x] **Exhaustive Scanning**: Scans every character in the target secret word.
- [x] **Early Exit**: Immediately detects incomplete words and returns boolean status accurately.

**Driver Verification Test**:  
Execute `is_word_guessed("ROBOT", ['R', 'O', 'B', 'T'])` -> verify `True`.  
Execute `is_word_guessed("ROBOT", ['R', 'O', 'B'])` -> verify `False`.

---

## Chapter 4: Visual Board & Defensive Input Pipeline

### 4.1 Formatted Board Rendering

**Alphabetical Guessed Letters & Visual Board**

Presenting information clearly is vital in CLI games. The player needs to see an organized list of previously guessed letters, their remaining lives, the current gallows illustration, and the masked word.

#### Task 5 — Format guessed letters display

Format previous guesses into an alphabetically sorted, comma-separated string:

Think of neatly arranging letter tiles in alphabetical order so the player can quickly see which letters they have already used.  
*Goal*: Return `"None"` if no letters have been guessed yet, or a sorted string like `"A, E, P, T"`.

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 1</span>
    <span class="step-title">Sort Guessed Letters Alphabetically</span>
  </div>
  <ul>
    <li>[ ] Check if <code>guessed_letters</code> is empty; if empty, return <code>"None"</code>.</li>
    <li>[ ] Sort a copy of the guessed letters collection in ascending alphabetical order.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 2</span>
    <span class="step-title">Construct Comma-Separated Guessed Letters String</span>
  </div>
  <ul>
    <li>[ ] Join the sorted letters with comma-space delimiters (<code>", "</code>) and return the resulting string.</li>
  </ul>
</div>

<div class="lang-tab python"><span class="lang-dot"></span>Python</div>

```python
# Task 5 - Format guessed letters display
# Step 1: Sort Guessed Letters Alphabetically
# Step 2: Construct Comma-Separated Guessed Letters String
def format_guessed_letters(guessed_letters):
    if not guessed_letters:
        return "None"
    sorted_letters = sorted(list(guessed_letters))
    return ", ".join(sorted_letters)
```

<div class="lang-tab cpp"><span class="lang-dot"></span>C++</div>

```cpp
// Task 5 - Format guessed letters display
// Step 1: Sort Guessed Letters Alphabetically
// Step 2: Construct Comma-Separated Guessed Letters String
string formatGuessedLetters(const vector<char>& guessedLetters) {
    if (guessedLetters.empty()) {
        return "None";
    }
    vector<char> sortedGuesses = guessedLetters;
    sort(sortedGuesses.begin(), sortedGuesses.end());
    string result = "";
    for (size_t i = 0; i < sortedGuesses.size(); ++i) {
        result += sortedGuesses[i];
        if (i + 1 < sortedGuesses.size()) {
            result += ", ";
        }
    }
    return result;
}
```

<div class="lang-tab java"><span class="lang-dot"></span>Java</div>

```java
// Task 5 - Format guessed letters display
// Step 1: Sort Guessed Letters Alphabetically
// Step 2: Construct Comma-Separated Guessed Letters String
public static String formatGuessedLetters(List<Character> guessedLetters) {
    if (guessedLetters.isEmpty()) {
        return "None";
    }
    List<Character> sortedGuesses = new ArrayList<>(guessedLetters);
    Collections.sort(sortedGuesses);
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < sortedGuesses.size(); i++) {
        sb.append(sortedGuesses.get(i));
        if (i + 1 < sortedGuesses.size()) {
            sb.append(", ");
        }
    }
    return sb.toString();
}
```

### Milestone Checkpoint: Guessed Letters Formatter Functional!

You have created a clean presentation helper for used letters:

- [x] **Empty Handling**: Displays `"None"` when no guesses have been registered.
- [x] **Alphabetical Ordering**: Always sorts letters predictably for rapid visual scanning.

**Driver Verification Test**:  
Execute `format_guessed_letters([])` -> verify `"None"`.  
Execute `format_guessed_letters(['Z', 'A', 'M'])` -> verify `"A, M, Z"`.

---

#### Task 6 — Render gallows and full game board

Display the complete visual state of the game board in the console:

Think of updating an electronic scoreboard that shows the gallows diagram, current masked word, used letters, and lives remaining.  
*Goal*: Print the ASCII art stage, the masked word, previous guesses, and remaining lives count.

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 1</span>
    <span class="step-title">Print Gallows ASCII Stage for Current Mistake Count</span>
  </div>
  <ul>
    <li>[ ] Access <code>STAGES[wrong_guesses]</code> and print the corresponding ASCII illustration.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 2</span>
    <span class="step-title">Print Masked Word Display</span>
  </div>
  <ul>
    <li>[ ] Call <code>get_masked_word(secret_word, guessed_letters)</code> and print the formatted word line.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 3</span>
    <span class="step-title">Print Formatted Guessed Letters</span>
  </div>
  <ul>
    <li>[ ] Call <code>format_guessed_letters(guessed_letters)</code> and print the guessed letters line.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 4</span>
    <span class="step-title">Print Remaining Lives Tally</span>
  </div>
  <ul>
    <li>[ ] Calculate <code>lives_left = MAX_LIVES - wrong_guesses</code> and print <code>Lives remaining: {lives_left} / {MAX_LIVES}</code>.</li>
  </ul>
</div>

<div class="lang-tab python"><span class="lang-dot"></span>Python</div>

```python
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
```

<div class="lang-tab cpp"><span class="lang-dot"></span>C++</div>

```cpp
// Task 6 - Render gallows and full game board
// Step 1: Print Gallows ASCII Stage for Current Mistake Count
// Step 2: Print Masked Word Display
// Step 3: Print Formatted Guessed Letters
// Step 4: Print Remaining Lives Tally
void displayBoard(int wrongGuesses, const string& secretWord, const vector<char>& guessedLetters) {
    cout << "\n" << STAGES[wrongGuesses] << "\n";
    cout << "\nWord: " << getMaskedWord(secretWord, guessedLetters) << "\n";
    cout << "Guessed letters: " << formatGuessedLetters(guessedLetters) << "\n";
    int livesLeft = MAX_LIVES - wrongGuesses;
    cout << "Lives remaining: " << livesLeft << " / " << MAX_LIVES << "\n";
}
```

<div class="lang-tab java"><span class="lang-dot"></span>Java</div>

```java
// Task 6 - Render gallows and full game board
// Step 1: Print Gallows ASCII Stage for Current Mistake Count
// Step 2: Print Masked Word Display
// Step 3: Print Formatted Guessed Letters
// Step 4: Print Remaining Lives Tally
public static void displayBoard(int wrongGuesses, String secretWord, List<Character> guessedLetters) {
    System.out.println("\n" + STAGES[wrongGuesses]);
    System.out.println("\nWord: " + getMaskedWord(secretWord, guessedLetters));
    System.out.println("Guessed letters: " + formatGuessedLetters(guessedLetters));
    int livesLeft = MAX_LIVES - wrongGuesses;
    System.out.println("Lives remaining: " + livesLeft + " / " + MAX_LIVES);
}
```

### Milestone Checkpoint: Visual Board Display Operational!

You have assembled the complete game state visualizer:

- [x] **Visual State Integration**: Combines gallows art, masked word, used letters, and lives.
- [x] **Mistake Indexing**: Dynamically maps mistakes directly to ASCII gallows stages.

**Driver Verification Test**:  
Execute `display_board(2, "PYTHON", ['P', 'O'])`. Verify that stage 2 (head + torso) is printed with `"Word: P _ _ _ O _"`, `"Guessed letters: O, P"`, and `"Lives remaining: 4 / 6"`.

---

### 4.2 Defensive Input Validation Engine

**Defensive Programming: CLI Input Validation**

Players can type anything into a terminal: lowercase letters, multiple letters, symbols, numbers, or empty strings. A robust application must never crash when unexpected input is received. We build a modular 3-stage validation pipeline:
1. Read raw text and normalize to uppercase.
2. Validate that input is exactly 1 alphabetic character.
3. Check against already guessed letters and prompt until valid.

#### Task 7 — Read and normalize letter input

Prompt the player and convert raw text into an uppercase character string:

Think of a clerk asking for an ID and immediately recording the letters in clean capital print.  
*Goal*: Read a line of terminal input, trim surrounding whitespace, and convert to uppercase.

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 1</span>
    <span class="step-title">Prompt Player for Guess Input</span>
  </div>
  <ul>
    <li>[ ] Display the input prompt <code>"\nEnter your guess (a single letter): "</code> without a trailing newline.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 2</span>
    <span class="step-title">Trim Whitespace and Convert to Uppercase</span>
  </div>
  <ul>
    <li>[ ] Read user input, trim leading/trailing whitespace, and convert characters to uppercase.</li>
  </ul>
</div>

<div class="lang-tab python"><span class="lang-dot"></span>Python</div>

```python
# Task 7 - Read and normalize letter input
# Step 1: Prompt Player for Guess Input
# Step 2: Trim Whitespace and Convert to Uppercase
def read_raw_guess():
    raw_text = input("\nEnter your guess (a single letter): ")
    return raw_text.strip().upper()
```

<div class="lang-tab cpp"><span class="lang-dot"></span>C++</div>

```cpp
// Task 7 - Read and normalize letter input
// Step 1: Prompt Player for Guess Input
// Step 2: Trim Whitespace and Convert to Uppercase
string readRawGuess() {
    cout << "\nEnter your guess (a single letter): ";
    string input;
    getline(cin, input);
    size_t start = input.find_first_not_of(" \t\r\n");
    size_t end = input.find_last_not_of(" \t\r\n");
    if (start == string::npos) {
        return "";
    }
    string trimmed = input.substr(start, end - start + 1);
    for (char& c : trimmed) {
        c = static_cast<char>(toupper(static_cast<unsigned char>(c)));
    }
    return trimmed;
}
```

<div class="lang-tab java"><span class="lang-dot"></span>Java</div>

```java
// Task 7 - Read and normalize letter input
// Step 1: Prompt Player for Guess Input
// Step 2: Trim Whitespace and Convert to Uppercase
public static String readRawGuess(Scanner scanner) {
    System.out.print("\nEnter your guess (a single letter): ");
    String input = scanner.nextLine().trim();
    return input.toUpperCase();
}
```

### Milestone Checkpoint: Raw Input Capture Operational!

You have built the input reader and normalizer:

- [x] **Prompt Presentation**: Clearly prompts player for a single letter.
- [x] **Case & Whitespace Normalization**: Automatically trims spaces and converts to uppercase.

---

#### Task 8 — Validate character format

Verify that the input consists of exactly one alphabetic character (A-Z):

Think of a turnstile gate that only permits a single, valid coin to pass through.  
*Goal*: Return `True` if the string length is 1 and the character is alphabetic, `False` otherwise.

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 1</span>
    <span class="step-title">Verify Exactly One Character Length</span>
  </div>
  <ul>
    <li>[ ] Check if the string length equals <code>1</code>.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 2</span>
    <span class="step-title">Verify Character is Alphabetic</span>
  </div>
  <ul>
    <li>[ ] Check if the single character is an alphabetic letter (A through Z).</li>
  </ul>
</div>

<div class="lang-tab python"><span class="lang-dot"></span>Python</div>

```python
# Task 8 - Validate character format
# Step 1: Verify Exactly One Character Length
# Step 2: Verify Character is Alphabetic
def is_valid_format(guess):
    return len(guess) == 1 and guess.isalpha()
```

<div class="lang-tab cpp"><span class="lang-dot"></span>C++</div>

```cpp
// Task 8 - Validate character format
// Step 1: Verify Exactly One Character Length
// Step 2: Verify Character is Alphabetic
bool isValidFormat(const string& guess) {
    return guess.size() == 1 && isalpha(static_cast<unsigned char>(guess[0]));
}
```

<div class="lang-tab java"><span class="lang-dot"></span>Java</div>

```java
// Task 8 - Validate character format
// Step 1: Verify Exactly One Character Length
// Step 2: Verify Character is Alphabetic
public static boolean isValidFormat(String guess) {
    return guess.length() == 1 && Character.isLetter(guess.charAt(0));
}
```

### Milestone Checkpoint: Character Format Validation Functional!

You have built the single-character validator:

- [x] **Length Guard**: Rejects empty strings, multiple letters, and whole words.
- [x] **Alpha Guard**: Rejects numbers, punctuation, and special characters.

**Driver Verification Test**:  
Verify `is_valid_format("A")` is `True`. Verify `is_valid_format("AB")`, `is_valid_format("1")`, and `is_valid_format("")` are `False`.

---

#### Task 9 — Check duplicates and finalize guess input

Combine format validation with duplicate checking in an interactive retry loop:

Think of a friendly referee checking the rulebook: if you type something invalid or repeat a move, they patiently ask you to try again.  
*Goal*: Re-prompt the user until they supply a new, un-guessed uppercase letter.

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 1</span>
    <span class="step-title">Verify Letter Has Not Been Guessed Yet</span>
  </div>
  <ul>
    <li>[ ] Check if the sanitized candidate letter already exists in <code>guessed_letters</code>.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 2</span>
    <span class="step-title">Output Friendly Duplicate Notification</span>
  </div>
  <ul>
    <li>[ ] If duplicate, print <code>"You already guessed '{letter}'. Try a different letter."</code>.</li>
    <li>[ ] If invalid format, print <code>"Invalid input. Please enter exactly one alphabetic letter (A-Z)."</code>.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 3</span>
    <span class="step-title">Loop Until Valid Unique Letter Received</span>
  </div>
  <ul>
    <li>[ ] Wrap in a <code>while True</code> loop and return the valid letter as soon as all conditions pass.</li>
  </ul>
</div>

<div class="lang-tab python"><span class="lang-dot"></span>Python</div>

```python
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
```

<div class="lang-tab cpp"><span class="lang-dot"></span>C++</div>

```cpp
// Task 9 - Check duplicates and finalize guess input
// Step 1: Verify Letter Has Not Been Guessed Yet
// Step 2: Output Friendly Duplicate Notification
// Step 3: Loop Until Valid Unique Letter Received
char getValidGuess(const vector<char>& guessedLetters) {
    while (true) {
        string raw = readRawGuess();
        if (!isValidFormat(raw)) {
            cout << "Invalid input. Please enter exactly one alphabetic letter (A-Z).\n";
            continue;
        }
        char letter = raw[0];
        bool alreadyGuessed = false;
        for (char g : guessedLetters) {
            if (g == letter) {
                alreadyGuessed = true;
                break;
            }
        }
        if (alreadyGuessed) {
            cout << "You already guessed '" << letter << "'. Try a different letter.\n";
        } else {
            return letter;
        }
    }
}
```

<div class="lang-tab java"><span class="lang-dot"></span>Java</div>

```java
// Task 9 - Check duplicates and finalize guess input
// Step 1: Verify Letter Has Not Been Guessed Yet
// Step 2: Output Friendly Duplicate Notification
// Step 3: Loop Until Valid Unique Letter Received
public static char getValidGuess(Scanner scanner, List<Character> guessedLetters) {
    while (true) {
        String raw = readRawGuess(scanner);
        if (!isValidFormat(raw)) {
            System.out.println("Invalid input. Please enter exactly one alphabetic letter (A-Z).");
            continue;
        }
        char letter = raw.charAt(0);
        if (guessedLetters.contains(letter)) {
            System.out.println("You already guessed '" + letter + "'. Try a different letter.");
        } else {
            return letter;
        }
    }
}
```

### Milestone Checkpoint: Defensive Guess Pipeline Complete!

You have completed the bulletproof CLI input subsystem:

- [x] **Input Sanitation**: Trims whitespace and enforces single alphabetic character rules.
- [x] **Duplicate Defense**: Prohibits wasting turns on repeated guesses.
- [x] **Continuous Retry**: Re-prompts smoothly without crashes.

---

## Chapter 5: Building the Game Engine (Thinking in OOP)

### 5.1 Game State & Reset Mechanics

**State Encapsulation in Hangman Class**

Now that all standalone utilities are operational, we encapsulate the dynamic round data inside a dedicated `Hangman` class. This class maintains the active mystery word, guessed letters, and wrong guesses counter.

#### Task 10 — Create the Hangman class constructor

Initialize the `Hangman` class attributes and state variables:

Think of preparing a blank game sheet before a word has been chosen: empty secret word, empty guess list, zero mistakes.  
*Goal*: Create the `Hangman` class with initialized attributes.

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 1</span>
    <span class="step-title">Initialize Secret Word Attribute</span>
  </div>
  <ul>
    <li>[ ] Initialize instance attribute <code>self.secret_word = ""</code> (or <code>secretWord = ""</code>).</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 2</span>
    <span class="step-title">Initialize Guessed Letters Collection Attribute</span>
  </div>
  <ul>
    <li>[ ] Initialize instance attribute <code>self.guessed_letters = []</code> (or empty collection).</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 3</span>
    <span class="step-title">Initialize Wrong Guesses Counter Attribute</span>
  </div>
  <ul>
    <li>[ ] Initialize instance attribute <code>self.wrong_guesses = 0</code> (or <code>wrongGuesses = 0</code>).</li>
  </ul>
</div>

<div class="lang-tab python"><span class="lang-dot"></span>Python</div>

```python
# Task 10 - Create the Hangman class constructor
class Hangman:
    def __init__(self):
        # Step 1: Initialize Secret Word Attribute
        self.secret_word = ""
        # Step 2: Initialize Guessed Letters Collection Attribute
        self.guessed_letters = []
        # Step 3: Initialize Wrong Guesses Counter Attribute
        self.wrong_guesses = 0
```

<div class="lang-tab cpp"><span class="lang-dot"></span>C++</div>

```cpp
// Task 10 - Create the Hangman class constructor
class Hangman {
public:
    string secretWord;
    vector<char> guessedLetters;
    int wrongGuesses;

    Hangman() {
        // Step 1: Initialize Secret Word Attribute
        secretWord = "";
        // Step 2: Initialize Guessed Letters Collection Attribute
        guessedLetters.clear();
        // Step 3: Initialize Wrong Guesses Counter Attribute
        wrongGuesses = 0;
    }
```

<div class="lang-tab java"><span class="lang-dot"></span>Java</div>

```java
// Task 10 - Create the Hangman class constructor
public class Hangman {
    String secretWord;
    List<Character> guessedLetters;
    int wrongGuesses;
    Random random;
    Scanner scanner;

    public Hangman() {
        // Step 1: Initialize Secret Word Attribute
        this.secretWord = "";
        // Step 2: Initialize Guessed Letters Collection Attribute
        this.guessedLetters = new ArrayList<>();
        // Step 3: Initialize Wrong Guesses Counter Attribute
        this.wrongGuesses = 0;
        this.random = new Random();
        this.scanner = new Scanner(System.in);
    }
```

### Milestone Checkpoint: Hangman State Initialized!

You have created the object-oriented state holder:

- [x] **State Encapsulation**: Cleanly bundles secret word, guessed letters, and wrong guesses count.
- [x] **Safe Initialization**: Initializes empty containers and zeroed counters.

---

#### Task 11 — Implement word selection and game reset

Select a new random secret word and clear round variables for a fresh match:

Think of shuffling a deck of word cards, drawing a new card face-down, and clearing the chalkboard.  
*Goal*: Set `secret_word` to a randomly chosen item from `WORDS`, clear `guessed_letters`, and reset `wrong_guesses` to 0.

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 1</span>
    <span class="step-title">Pick Random Word from Word Pool</span>
  </div>
  <ul>
    <li>[ ] Use the language random generator to choose a random word from <code>WORDS</code> and assign it to <code>secret_word</code>.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 2</span>
    <span class="step-title">Reset Guessed Letters Collection</span>
  </div>
  <ul>
    <li>[ ] Clear all elements in <code>guessed_letters</code> so it becomes an empty list.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 3</span>
    <span class="step-title">Reset Wrong Guesses Counter to Zero</span>
  </div>
  <ul>
    <li>[ ] Set <code>wrong_guesses = 0</code>.</li>
  </ul>
</div>

<div class="lang-tab python"><span class="lang-dot"></span>Python</div>

```python
    # Task 11 - Implement word selection and game reset
    def reset_game(self):
        # Step 1: Pick Random Word from Word Pool
        self.secret_word = random.choice(WORDS)
        # Step 2: Reset Guessed Letters Collection
        self.guessed_letters = []
        # Step 3: Reset Wrong Guesses Counter to Zero
        self.wrong_guesses = 0
```

<div class="lang-tab cpp"><span class="lang-dot"></span>C++</div>

```cpp
    // Task 11 - Implement word selection and game reset
    void resetGame() {
        // Step 1: Pick Random Word from Word Pool
        int index = rand() % WORDS.size();
        secretWord = WORDS[index];
        // Step 2: Reset Guessed Letters Collection
        guessedLetters.clear();
        // Step 3: Reset Wrong Guesses Counter to Zero
        wrongGuesses = 0;
    }
```

<div class="lang-tab java"><span class="lang-dot"></span>Java</div>

```java
    // Task 11 - Implement word selection and game reset
    public void resetGame() {
        // Step 1: Pick Random Word from Word Pool
        int index = random.nextInt(WORDS.length);
        secretWord = WORDS[index];
        // Step 2: Reset Guessed Letters Collection
        guessedLetters.clear();
        // Step 3: Reset Wrong Guesses Counter to Zero
        wrongGuesses = 0;
    }
```

### Milestone Checkpoint: Game Reset & Word Selection Operational!

You have implemented dynamic word picking and session reset:

- [x] **Word Randomization**: Picks unpredictable target words from `WORDS`.
- [x] **State Sanitation**: Flushes prior match history cleanly.

**Driver Verification Test**:  
Instantiate `game = Hangman()` and call `reset_game()`. Verify `game.secret_word in WORDS`, `len(game.guessed_letters) == 0`, and `game.wrong_guesses == 0`.

---

### 5.2 Guess Processing & Outcome Resolution

**Registering Letters & Decrementing Lives**

When a player inputs a valid letter, two actions must occur:
1. The letter is added to `guessed_letters`.
2. If the letter is in `secret_word`, praise the player; if not, increment `wrong_guesses` and notify the player.

#### Task 12 — Implement single guess processing

Process an individual letter guess and update game state:

Think of checking if a guessed letter appears on the puzzle board: if yes, celebrate; if no, draw the next part of the gallows figure.  
*Goal*: Append `letter` to `guessed_letters`, check membership in `secret_word`, and update `wrong_guesses` accordingly.

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 1</span>
    <span class="step-title">Register Letter in Guessed Letters Collection</span>
  </div>
  <ul>
    <li>[ ] Append the validated <code>letter</code> parameter to <code>self.guessed_letters</code>.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 2</span>
    <span class="step-title">Branch on Match: Announce Correct Guess</span>
  </div>
  <ul>
    <li>[ ] If <code>letter in self.secret_word</code>, print <code>"\nGood guess! '{letter}' is in the word!"</code>.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 3</span>
    <span class="step-title">Branch on Miss: Increment Wrong Guesses and Announce Miss</span>
  </div>
  <ul>
    <li>[ ] Otherwise, increment <code>self.wrong_guesses += 1</code> and print <code>"\nSorry! '{letter}' is not in the word."</code>.</li>
  </ul>
</div>

<div class="lang-tab python"><span class="lang-dot"></span>Python</div>

```python
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
```

<div class="lang-tab cpp"><span class="lang-dot"></span>C++</div>

```cpp
    // Task 12 - Implement single guess processing
    void processGuess(char letter) {
        // Step 1: Register Letter in Guessed Letters Collection
        guessedLetters.push_back(letter);
        // Step 2: Branch on Match: Announce Correct Guess
        if (secretWord.find(letter) != string::npos) {
            cout << "\nGood guess! '" << letter << "' is in the word!\n";
        }
        // Step 3: Branch on Miss: Increment Wrong Guesses and Announce Miss
        else {
            wrongGuesses++;
            cout << "\nSorry! '" << letter << "' is not in the word.\n";
        }
    }
```

<div class="lang-tab java"><span class="lang-dot"></span>Java</div>

```java
    // Task 12 - Implement single guess processing
    public void processGuess(char letter) {
        // Step 1: Register Letter in Guessed Letters Collection
        guessedLetters.add(letter);
        // Step 2: Branch on Match: Announce Correct Guess
        if (secretWord.indexOf(letter) >= 0) {
            System.out.println("\nGood guess! '" + letter + "' is in the word!");
        }
        // Step 3: Branch on Miss: Increment Wrong Guesses and Announce Miss
        else {
            wrongGuesses++;
            System.out.println("\nSorry! '" + letter + "' is not in the word.");
        }
    }
```

### Milestone Checkpoint: Guess Processing & Lives Deduction Verified!

You have implemented round state mutations:

- [x] **Guess Registration**: Accurately tracks every player attempt.
- [x] **Lives Deduction**: Increments mistake counter solely when a wrong letter is supplied.
- [x] **Immediate Feedback**: Gives instant verbal feedback on success or miss.

**Driver Verification Test**:  
Set `game.secret_word = "ROBOT"`. Call `game.process_guess("O")` -> verify `game.wrong_guesses == 0`. Call `game.process_guess("Z")` -> verify `game.wrong_guesses == 1`.

---

#### Task 13 — Announce outcome and reveal secret word

Render the final board state and announce whether the player won or ran out of lives:

Think of the tournament master delivering the final verdict: cheering the champion or revealing the answer that got away.  
*Goal*: Render the final board, check `is_word_guessed()`, and print the appropriate victory or game-over banner.

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 1</span>
    <span class="step-title">Render Final Game Board State</span>
  </div>
  <ul>
    <li>[ ] Call <code>display_board(self.wrong_guesses, self.secret_word, self.guessed_letters)</code> to show the final board appearance.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 2</span>
    <span class="step-title">Evaluate Victory Condition and Congratulate Player</span>
  </div>
  <ul>
    <li>[ ] If <code>is_word_guessed()</code> is <code>True</code>, print <code>"\nCONGRATULATIONS! You solved the secret word: {self.secret_word}!"</code>.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 3</span>
    <span class="step-title">Evaluate Defeat Condition and Reveal Secret Word</span>
  </div>
  <ul>
    <li>[ ] Otherwise, print <code>"\nGAME OVER! You ran out of lives. The secret word was: {self.secret_word}."</code>.</li>
  </ul>
</div>

<div class="lang-tab python"><span class="lang-dot"></span>Python</div>

```python
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
```

<div class="lang-tab cpp"><span class="lang-dot"></span>C++</div>

```cpp
    // Task 13 - Announce outcome and reveal secret word
    void announceResult() const {
        // Step 1: Render Final Game Board State
        displayBoard(wrongGuesses, secretWord, guessedLetters);
        // Step 2: Evaluate Victory Condition and Congratulate Player
        if (isWordGuessed(secretWord, guessedLetters)) {
            cout << "\nCONGRATULATIONS! You solved the secret word: " << secretWord << "!\n";
        }
        // Step 3: Evaluate Defeat Condition and Reveal Secret Word
        else {
            cout << "\nGAME OVER! You ran out of lives. The secret word was: " << secretWord << ".\n";
        }
    }
```

<div class="lang-tab java"><span class="lang-dot"></span>Java</div>

```java
    // Task 13 - Announce outcome and reveal secret word
    public void announceResult() {
        // Step 1: Render Final Game Board State
        displayBoard(wrongGuesses, secretWord, guessedLetters);
        // Step 2: Evaluate Victory Condition and Congratulate Player
        if (isWordGuessed(secretWord, guessedLetters)) {
            System.out.println("\nCONGRATULATIONS! You solved the secret word: " + secretWord + "!");
        }
        // Step 3: Evaluate Defeat Condition and Reveal Secret Word
        else {
            System.out.println("\nGAME OVER! You ran out of lives. The secret word was: " + secretWord + ".");
        }
    }
```

### Milestone Checkpoint: Game Outcome Presentation Operational!

You have implemented outcome resolution:

- [x] **Final Board Synchronization**: Guarantees the player sees the full completed or failed board.
- [x] **Closure & Word Reveal**: Always informs the player of the mystery word upon defeat.

---

### 5.3 Single-Game Turn Loop

**Turn-Based Lifecycle Architecture**

A single match orchestrates the full turn lifecycle: resetting state, displaying the match banner, and repeatedly presenting the board, reading guesses, and updating state until either the word is solved or 6 mistakes have accumulated.

#### Task 14 — Construct single-game turn loop

Tie all round mechanisms together into `play_round()`:

Think of the conductor leading an orchestra through every movement of a symphony until the finale.  
*Goal*: Drive the turn loop while `wrong_guesses < MAX_LIVES` and `not is_word_guessed()`.

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 1</span>
    <span class="step-title">Reset Game State for New Match</span>
  </div>
  <ul>
    <li>[ ] Call <code>self.reset_game()</code> to pick a new secret word and clear counters.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 2</span>
    <span class="step-title">Print Match Start Banner</span>
  </div>
  <ul>
    <li>[ ] Print <code>"\n===== NEW HANGMAN GAME ====="</code> and the secret word length indicator.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 3</span>
    <span class="step-title">Run Turn Loop While Alive and Unsolved</span>
  </div>
  <ul>
    <li>[ ] While <code>self.wrong_guesses &lt; MAX_LIVES</code> and <code>not is_word_guessed(self.secret_word, self.guessed_letters)</code>:</li>
    <li>[ ] Render board via <code>display_board(self.wrong_guesses, self.secret_word, self.guessed_letters)</code>, collect guess via <code>get_valid_guess(self.guessed_letters)</code>, and process guess via <code>self.process_guess(guess)</code>.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 4</span>
    <span class="step-title">Call Outcome Announcer</span>
  </div>
  <ul>
    <li>[ ] After loop exit, call <code>self.announce_result()</code>.</li>
  </ul>
</div>

<div class="lang-tab python"><span class="lang-dot"></span>Python</div>

```python
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
```

<div class="lang-tab cpp"><span class="lang-dot"></span>C++</div>

```cpp
    // Task 14 - Construct single-game turn loop
    void playRound() {
        // Step 1: Reset Game State for New Match
        resetGame();
        // Step 2: Print Match Start Banner
        cout << "\n===== NEW HANGMAN GAME =====\n";
        cout << "A secret word has been chosen with " << secretWord.size() << " letters. Good luck!\n";

        // Step 3: Run Turn Loop While Alive and Unsolved
        while (wrongGuesses < MAX_LIVES && !isWordGuessed(secretWord, guessedLetters)) {
            displayBoard(wrongGuesses, secretWord, guessedLetters);
            char guess = getValidGuess(guessedLetters);
            processGuess(guess);
        }

        // Step 4: Call Outcome Announcer
        announceResult();
    }
```

<div class="lang-tab java"><span class="lang-dot"></span>Java</div>

```java
    // Task 14 - Construct single-game turn loop
    public void playRound() {
        // Step 1: Reset Game State for New Match
        resetGame();
        // Step 2: Print Match Start Banner
        System.out.println("\n===== NEW HANGMAN GAME =====");
        System.out.println("A secret word has been chosen with " + secretWord.length() + " letters. Good luck!");

        // Step 3: Run Turn Loop While Alive and Unsolved
        while (wrongGuesses < MAX_LIVES && !isWordGuessed(secretWord, guessedLetters)) {
            displayBoard(wrongGuesses, secretWord, guessedLetters);
            char guess = getValidGuess(scanner, guessedLetters);
            processGuess(guess);
        }

        // Step 4: Call Outcome Announcer
        announceResult();
    }
```

### Milestone Checkpoint: Single-Game Turn Loop Complete!

You have built the complete single-game turn coordinator:

- [x] **Loop Boundary Integrity**: Never allows turns past 6 mistakes or after the word is solved.
- [x] **Complete Workflow**: Orchestrates reset, turn presentation, guess processing, and final announcement.

---

## Chapter 6: Adding Replayability & Full Application Execution

### 6.1 Session Management

**Continuous Gaming & Rematch Loops**

For a polished user experience, players should be able to play multiple games in a single session without having to restart the script from the terminal. We build an interactive rematch prompt and a multi-game session loop.

#### Task 15 — Implement rematch prompt

Ask the player if they wish to play again, validating `"y"` or `"n"`:

Think of an arcade machine flashing "CONTINUE? (Y/N)" after a game ends.  
*Goal*: Return `True` if the user confirms replay (`"y"`), `False` if they decline (`"n"`), and re-prompt on invalid input.

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 1</span>
    <span class="step-title">Run Interactive Replay Prompt Loop</span>
  </div>
  <ul>
    <li>[ ] Start a <code>while True</code> loop prompting <code>"\nPlay again? (y/n): "</code>.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 2</span>
    <span class="step-title">Read and Normalize Confirmation Input</span>
  </div>
  <ul>
    <li>[ ] Read user response, strip whitespace, and convert to lowercase.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 3</span>
    <span class="step-title">Return Boolean Replay Decision</span>
  </div>
  <ul>
    <li>[ ] Return <code>True</code> if <code>"y"</code>; return <code>False</code> if <code>"n"</code>; otherwise print <code>"Please type y or n."</code> and re-prompt.</li>
  </ul>
</div>

<div class="lang-tab python"><span class="lang-dot"></span>Python</div>

```python
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
```

<div class="lang-tab cpp"><span class="lang-dot"></span>C++</div>

```cpp
    // Task 15 - Implement rematch prompt
    static bool askReplay() {
        // Step 1: Run Interactive Replay Prompt Loop
        while (true) {
            // Step 2: Read and Normalize Confirmation Input
            cout << "\nPlay again? (y/n): ";
            string answer;
            getline(cin, answer);
            size_t start = answer.find_first_not_of(" \t\r\n");
            size_t end = answer.find_last_not_of(" \t\r\n");
            string trimmed = (start == string::npos) ? "" : answer.substr(start, end - start + 1);
            for (char& c : trimmed) {
                c = static_cast<char>(tolower(static_cast<unsigned char>(c)));
            }
            // Step 3: Return Boolean Replay Decision
            if (trimmed == "y") {
                return true;
            }
            if (trimmed == "n") {
                return false;
            }
            cout << "Please type y or n.\n";
        }
    }
```

<div class="lang-tab java"><span class="lang-dot"></span>Java</div>

```java
    // Task 15 - Implement rematch prompt
    public static boolean askReplay(Scanner scanner) {
        // Step 1: Run Interactive Replay Prompt Loop
        while (true) {
            // Step 2: Read and Normalize Confirmation Input
            System.out.print("\nPlay again? (y/n): ");
            String answer = scanner.nextLine().trim().toLowerCase();
            // Step 3: Return Boolean Replay Decision
            if (answer.equals("y")) {
                return true;
            }
            if (answer.equals("n")) {
                return false;
            }
            System.out.println("Please type y or n.");
        }
    }
```

### Milestone Checkpoint: Rematch Prompt Functional!

You have implemented the replay inquiry mechanism:

- [x] **Case-Insensitive Normalization**: Accepts upper or lowercase input cleanly.
- [x] **Defensive Guard**: Politely rejects invalid input and re-prompts without exiting.

---

#### Task 16 — Construct multi-game session loop

Wrap `play_round()` in a continuous multi-match session controller:

Think of sitting down for a complete tournament session, playing as many rounds as you want until you decide to walk away.  
*Goal*: Run an indefinite loop calling `play_round()`, checking `ask_replay()`, and exiting with a farewell message when finished.

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 1</span>
    <span class="step-title">Run Indefinite Session Loop</span>
  </div>
  <ul>
    <li>[ ] Start an indefinite <code>while True</code> loop in method <code>play_many()</code>.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 2</span>
    <span class="step-title">Execute Game Lifecycle</span>
  </div>
  <ul>
    <li>[ ] Call <code>self.play_round()</code> to run a complete game match.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 3</span>
    <span class="step-title">Prompt for Rematch Confirmation</span>
  </div>
  <ul>
    <li>[ ] Call <code>not self.ask_replay()</code> to evaluate if the player wishes to stop.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 4</span>
    <span class="step-title">Print Session Farewell on Exit</span>
  </div>
  <ul>
    <li>[ ] Print <code>"\nThanks for playing Hangman!"</code> and break out of the session loop.</li>
  </ul>
</div>

<div class="lang-tab python"><span class="lang-dot"></span>Python</div>

```python
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
```

<div class="lang-tab cpp"><span class="lang-dot"></span>C++</div>

```cpp
    // Task 16 - Construct multi-game session loop
    void playMany() {
        // Step 1: Run Indefinite Session Loop
        while (true) {
            // Step 2: Execute Game Lifecycle
            playRound();
            // Step 3: Prompt for Rematch Confirmation
            if (!askReplay()) {
                // Step 4: Print Session Farewell on Exit
                cout << "\nThanks for playing Hangman!\n";
                break;
            }
        }
    }
};
```

<div class="lang-tab java"><span class="lang-dot"></span>Java</div>

```java
    // Task 16 - Construct multi-game session loop
    public void playMany() {
        // Step 1: Run Indefinite Session Loop
        while (true) {
            // Step 2: Execute Game Lifecycle
            playRound();
            // Step 3: Prompt for Rematch Confirmation
            if (!askReplay(scanner)) {
                // Step 4: Print Session Farewell on Exit
                System.out.println("\nThanks for playing Hangman!");
                break;
            }
        }
    }
```

### Milestone Checkpoint: Multi-Game Session Engine Complete!

You have completed the multi-round gameplay coordinator:

- [x] **Continuous Play**: Supports back-to-back puzzle rounds without restarting the program.
- [x] **Clean Termination**: Breaks out cleanly and prints a parting farewell.

---

### 6.2 Application Assembly

**Program Inception & Launch Pipeline**

With all classes, helpers, and state loops complete, the final step is to assemble the `main()` entry function to greet the user, instantiate the game engine, and launch the session.

#### Task 17 — Assemble the main() entry point

Wire the entire application together inside `main()`:

Think of turning the ignition key in an automobile: the engine hums to life, and the dashboard illuminates ready for your journey.  
*Goal*: Call `print_welcome()`, create a `Hangman` instance, and call `play_many()`.

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 1</span>
    <span class="step-title">Call Welcome Banner Function</span>
  </div>
  <ul>
    <li>[ ] Invoke <code>print_welcome()</code> (or <code>printWelcome()</code>).</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 2</span>
    <span class="step-title">Instantiate Hangman Game Manager</span>
  </div>
  <ul>
    <li>[ ] Create an instance of <code>Hangman</code> named <code>game</code>.</li>
  </ul>
</div>

<div class="step-card">
  <div class="step-header">
    <span class="step-badge">STEP 3</span>
    <span class="step-title">Launch Multi-Game Session Loop</span>
  </div>
  <ul>
    <li>[ ] Call <code>game.play_many()</code> (or <code>game.playMany()</code>) and add standard script execution guards.</li>
  </ul>
</div>

<div class="lang-tab python"><span class="lang-dot"></span>Python</div>

```python
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
```

<div class="lang-tab cpp"><span class="lang-dot"></span>C++</div>

```cpp
// Task 17 - Assemble the main() entry point
int main() {
    srand(static_cast<unsigned int>(time(nullptr)));

    // Step 1: Call Welcome Banner Function
    printWelcome();
    // Step 2: Instantiate Hangman Game Manager
    Hangman game;
    // Step 3: Launch Multi-Game Session Loop
    game.playMany();
    return 0;
}
```

<div class="lang-tab java"><span class="lang-dot"></span>Java</div>

```java
    // Task 17 - Assemble the main() entry point
    public static void main(String[] args) {
        // Step 1: Call Welcome Banner Function
        printWelcome();
        // Step 2: Instantiate Hangman Game Manager
        Hangman game = new Hangman();
        // Step 3: Launch Multi-Game Session Loop
        game.playMany();
    }
}
```

### Milestone Checkpoint: Full Application Experience Achieved!

You have completed the entire Hangman architecture:

- [x] **Unified Architecture**: All 17 tasks and 49 steps wired into a cohesive, production-grade CLI game.
- [x] **Tri-Language Parity**: Identical operational logic and structure across Python, C++, and Java.
- [x] **Complete Polish**: Defensive input parsing, ASCII art visualization, and seamless replay loops.

---

## Chapter 7: Reflect & Expand

### 7.1 What You Have Built

You have designed and constructed an interactive, object-oriented Hangman application from scratch. Take a moment to review the software engineering patterns and algorithmic foundations you practiced:

| Feature Dimension | Implementation Technique | Educational Value |
|---|---|---|
| **Constants & Boundaries** | `WORDS`, `MAX_LIVES`, `STAGES` | Eliminates hard-coded magic values; centralizes game difficulty configuration. |
| **String Masking** | Dynamic character-by-character evaluation | Teaches string concatenation, list filtering, and membership checks. |
| **Defensive Input** | 3-stage validation pipeline (`read`, `format`, `duplicates`) | Guards CLI applications against crashes caused by malformed user input. |
| **Terminal Graphics** | Progressive ASCII art stages | Visualizes numeric state changes into intuitive graphical representations. |
| **OOP Encapsulation** | `Hangman` class with instance state | Separates persistent round state from stateless functional utilities. |
| **Interactive Loops** | Multi-game replay coordinator | Demonstrates session management and continuous interactive user loops. |

---

### 7.2 Extension Ideas

Now that you have a functioning game engine, consider challenging yourself with these creative extensions:

1. **Difficulty Settings**: Add easy (8 lives), medium (6 lives), and hard (4 lives) modes with different word lists.
2. **Category Selection**: Allow players to pick word topics (such as Animals, Countries, Programming Languages, or Science).
3. **High Score Tracker**: Save win streaks and best completion times to a local JSON file across sessions.
4. **Hint System**: Allow the player to type `"?"` to reveal a single random unsolved letter at the cost of 2 lives.

---

### 7.3 Share What You Built! Time to Showcase Your Project!

Congratulations on completing Project 3! You now have a complete, polished portfolio project that demonstrates your understanding of object-oriented design and defensive programming.

- Push your repository to GitHub with a clean `README.md` and screenshot recordings.
- Share your code with fellow learners and explain how your 3-stage input pipeline prevents invalid character crashes.
- Explore running your implementation in Python, C++, and Java to appreciate the syntactic strengths of each language.

---

## Appendix: Full Pseudocode Reference

### Complete Tri-Language Algorithmic Logic

```text
PROGRAM HangmanGame:
    CONSTANT WORDS = ["PYTHON", "PLANET", "ROBOT", "GUITAR", "SILVER", "ROCKET", "CODING"]
    CONSTANT MAX_LIVES = 6
    CONSTANT STAGES = [7 ASCII art strings for mistakes 0 through 6]

    FUNCTION print_welcome():
        OUTPUT "Welcome to Hangman!"

    FUNCTION get_masked_word(secret_word, guessed_letters):
        SET display_chars = []
        FOR EACH letter IN secret_word:
            IF letter IN guessed_letters THEN
                APPEND letter TO display_chars
            ELSE
                APPEND "_" TO display_chars
            END IF
        END FOR
        RETURN JOIN display_chars WITH " "

    FUNCTION is_word_guessed(secret_word, guessed_letters):
        FOR EACH letter IN secret_word:
            IF letter NOT IN guessed_letters THEN
                RETURN False
            END IF
        END FOR
        RETURN True

    FUNCTION format_guessed_letters(guessed_letters):
        IF guessed_letters IS EMPTY THEN
            RETURN "None"
        END IF
        SET sorted_letters = SORT(guessed_letters)
        RETURN JOIN sorted_letters WITH ", "

    FUNCTION display_board(wrong_guesses, secret_word, guessed_letters):
        OUTPUT STAGES[wrong_guesses]
        OUTPUT "Word: " + get_masked_word(secret_word, guessed_letters)
        OUTPUT "Guessed letters: " + format_guessed_letters(guessed_letters)
        SET lives_left = MAX_LIVES - wrong_guesses
        OUTPUT "Lives remaining: " + lives_left + " / " + MAX_LIVES

    FUNCTION read_raw_guess():
        PROMPT "\nEnter your guess (a single letter): "
        READ user_input
        RETURN TRIM(UPPERCASE(user_input))

    FUNCTION is_valid_format(guess):
        RETURN LENGTH(guess) == 1 AND IS_ALPHA(guess)

    FUNCTION get_valid_guess(guessed_letters):
        WHILE True:
            SET guess = read_raw_guess()
            IF NOT is_valid_format(guess) THEN
                OUTPUT "Invalid input. Please enter exactly one alphabetic letter (A-Z)."
            ELSE IF guess IN guessed_letters THEN
                OUTPUT "You already guessed '" + guess + "'. Try a different letter."
            ELSE
                RETURN guess
            END IF
        END WHILE

    CLASS Hangman:
        CONSTRUCTOR:
            SET self.secret_word = ""
            SET self.guessed_letters = []
            SET self.wrong_guesses = 0

        METHOD reset_game():
            SET self.secret_word = RANDOM_CHOICE(WORDS)
            SET self.guessed_letters = []
            SET self.wrong_guesses = 0

        METHOD process_guess(letter):
            APPEND letter TO self.guessed_letters
            IF letter IN self.secret_word THEN
                OUTPUT "Good guess! '" + letter + "' is in the word!"
            ELSE
                SET self.wrong_guesses = self.wrong_guesses + 1
                OUTPUT "Sorry! '" + letter + "' is not in the word."
            END IF

        METHOD announce_result():
            CALL display_board(self.wrong_guesses, self.secret_word, self.guessed_letters)
            IF is_word_guessed(self.secret_word, self.guessed_letters) THEN
                OUTPUT "CONGRATULATIONS! You solved the secret word: " + self.secret_word + "!"
            ELSE
                OUTPUT "GAME OVER! You ran out of lives. The secret word was: " + self.secret_word + "."
            END IF

        METHOD play_round():
            CALL self.reset_game()
            OUTPUT "===== NEW HANGMAN GAME ====="
            OUTPUT "A secret word has been chosen with " + LENGTH(self.secret_word) + " letters. Good luck!"
            WHILE self.wrong_guesses < MAX_LIVES AND NOT is_word_guessed(self.secret_word, self.guessed_letters):
                CALL display_board(self.wrong_guesses, self.secret_word, self.guessed_letters)
                SET guess = CALL get_valid_guess(self.guessed_letters)
                CALL self.process_guess(guess)
            END WHILE
            CALL self.announce_result()

        METHOD ask_replay():
            WHILE True:
                PROMPT "Play again? (y/n): "
                READ answer
                SET normalized = TRIM(LOWERCASE(answer))
                IF normalized == "y" THEN
                    RETURN True
                ELSE IF normalized == "n" THEN
                    RETURN False
                ELSE
                    OUTPUT "Please type y or n."
                END IF
            END WHILE

        METHOD play_many():
            WHILE True:
                CALL self.play_round()
                IF NOT self.ask_replay() THEN
                    OUTPUT "Thanks for playing Hangman!"
                    BREAK
                END IF
            END WHILE

    FUNCTION main():
        CALL print_welcome()
        SET game = NEW Hangman()
        CALL game.play_many()

END PROGRAM
```
