#include <algorithm>
#include <cctype>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Task 1 - Create the entry file and print welcome message
// Step 1: Entry File Setup
// Step 2: Welcome Banner Output
void printWelcome() {
    cout << "Welcome to Hangman!\n";
}

// Task 2 - Define word pool, maximum lives, and gallows stages
// Step 1: Declare Secret Word Pool
const vector<string> WORDS = {"PYTHON", "PLANET", "ROBOT", "GUITAR", "SILVER", "ROCKET", "CODING"};

// Step 2: Declare Maximum Lives Threshold
const int MAX_LIVES = 6;

// Step 3: Declare Gallows ASCII Art Stages
const vector<string> STAGES = {
    // 0 mistakes (6 lives left)
    "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
    // 1 mistake (5 lives left)
    "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
    // 2 mistakes (4 lives left)
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
    // 3 mistakes (3 lives left)
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
    // 4 mistakes (2 lives left)
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
    // 5 mistakes (1 life left)
    "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
    // 6 mistakes (0 lives left - Game Over)
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
};

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

// Task 7 - Read and normalize letter input
// Step 1: Prompt Player for Guess Input
// Step 2: Trim Whitespace and Convert to Uppercase
string readRawGuess() {
    cout << "\nEnter your guess (a single letter): ";
    string input;
    getline(cin, input);
    // Trim whitespace
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

// Task 8 - Validate character format
// Step 1: Verify Exactly One Character Length
// Step 2: Verify Character is Alphabetic
bool isValidFormat(const string& guess) {
    return guess.size() == 1 && isalpha(static_cast<unsigned char>(guess[0]));
}

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
