import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class Hangman {

    // Task 1 - Create the entry file and print welcome message
    // Step 1: Entry File Setup
    // Step 2: Welcome Banner Output
    public static void printWelcome() {
        System.out.println("Welcome to Hangman!");
    }

    // Task 2 - Define word pool, maximum lives, and gallows stages
    // Step 1: Declare Secret Word Pool
    static final String[] WORDS = {"PYTHON", "PLANET", "ROBOT", "GUITAR", "SILVER", "ROCKET", "CODING"};

    // Step 2: Declare Maximum Lives Threshold
    static final int MAX_LIVES = 6;

    // Step 3: Declare Gallows ASCII Art Stages
    static final String[] STAGES = {
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

    // Task 7 - Read and normalize letter input
    // Step 1: Prompt Player for Guess Input
    // Step 2: Trim Whitespace and Convert to Uppercase
    public static String readRawGuess(Scanner scanner) {
        System.out.print("\nEnter your guess (a single letter): ");
        String input = scanner.nextLine().trim();
        return input.toUpperCase();
    }

    // Task 8 - Validate character format
    // Step 1: Verify Exactly One Character Length
    // Step 2: Verify Character is Alphabetic
    public static boolean isValidFormat(String guess) {
        return guess.length() == 1 && Character.isLetter(guess.charAt(0));
    }

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

    // Task 10 - Create the Hangman class constructor
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
