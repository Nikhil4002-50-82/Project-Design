// Task 1 - Create the entry file and print welcome message
// Step 1: Entry File Setup
import java.util.Random;
import java.util.Scanner;

public class StonePaperScissors {

    static void printWelcome() {
        // Step 2: Welcome Banner Output
        System.out.println("Welcome to Stone Paper Scissors!");
    }

    // Task 2 - Define valid moves and target score
    // Step 1: Declare Move Collection
    static final String[] MOVES = {"Stone", "Paper", "Scissors"};

    // Step 2: Declare Target Score Threshold
    static final int TARGET_SCORE = 3;

    // Task 3 - Create the RoundResult model
    static class RoundResult {
        // Step 1: Initialize Winner Identifier
        String winner;

        // Step 2: Initialize Outcome Reason
        String reason;

        RoundResult(String winner, String reason) {
            this.winner = winner;
            this.reason = reason;
        }
    }

    // Task 4 - Implement determineWinner(playerMove, systemMove)
    static RoundResult determineWinner(String playerMove, String systemMove) {
        // Step 1: Check Draw Condition
        if (playerMove.equals(systemMove)) {
            return new RoundResult("draw", "Both chose " + playerMove);
        }
        // Step 2: Check Player Victory Conditions
        else if (playerMove.equals("Stone") && systemMove.equals("Scissors")) {
            return new RoundResult("player", "Stone crushes Scissors");
        } else if (playerMove.equals("Scissors") && systemMove.equals("Paper")) {
            return new RoundResult("player", "Scissors cuts Paper");
        } else if (playerMove.equals("Paper") && systemMove.equals("Stone")) {
            return new RoundResult("player", "Paper covers Stone");
        }
        // Step 3: Check System Victory Conditions
        else if (systemMove.equals("Stone") && playerMove.equals("Scissors")) {
            return new RoundResult("system", "Stone crushes Scissors");
        } else if (systemMove.equals("Scissors") && playerMove.equals("Paper")) {
            return new RoundResult("system", "Scissors cuts Paper");
        } else {
            return new RoundResult("system", "Paper covers Stone");
        }
    }

    // Task 5 - Create the Player class constructor
    static class Player {
        String name;
        int score;

        Player(String rawName) {
            // Step 1: Sanitize Player Name
            String trimmed = (rawName == null) ? "" : rawName.trim();
            this.name = trimmed.isEmpty() ? "Player" : trimmed;

            // Step 2: Initialize Starting Score
            this.score = 0;
        }

        // Task 6 - Implement score reset on Player
        void resetScore() {
            // Step 1: Zero Out Score
            this.score = 0;
        }

        // Task 7 - Implement validated human move input
        String chooseMove(Scanner scanner) {
            // Step 1: Interactive Prompt Loop
            while (true) {
                // Step 2: Display Choice Menu
                System.out.println("\n" + name + ", choose your move:");
                System.out.println("  [1] Stone");
                System.out.println("  [2] Paper");
                System.out.println("  [3] Scissors");
                System.out.print("Enter choice (1-3): ");

                // Step 3: Read and Normalize Input
                if (!scanner.hasNextLine()) return "Stone";
                String input = scanner.nextLine().trim().toLowerCase();

                // Step 4: Validate and Map Choices
                if (input.equals("1") || input.equals("stone")) return "Stone";
                if (input.equals("2") || input.equals("paper")) return "Paper";
                if (input.equals("3") || input.equals("scissors")) return "Scissors";

                // Step 5: Handle Invalid Input
                System.out.println("Invalid input. Please enter 1, 2, or 3.");
            }
        }
    }

    // Task 8 - Create the SystemPlayer class skeleton
    static class SystemPlayer extends Player {
        private final Random random = new Random();

        SystemPlayer() {
            // Step 1: Subclass Player Entity
            super("System");
        }

        // Task 9 - Implement system random move choice
        String chooseMove() {
            // Step 1: Generate Random Move Selection
            int pick = random.nextInt(MOVES.length);

            // Step 2: Return Selected Move
            return MOVES[pick];
        }
    }

    // Task 10 - Create the Game class constructor
    static class Game {
        Player player;
        SystemPlayer system;
        int targetScore;
        Scanner scanner;

        Game(String playerName, Scanner scanner) {
            // Step 1: Instantiate Human Player
            this.player = new Player(playerName);

            // Step 2: Instantiate System Opponent
            this.system = new SystemPlayer();

            // Step 3: Initialize Target Score Threshold
            this.targetScore = TARGET_SCORE;
            this.scanner = scanner;
        }

        // Task 11 - Display the formatted scoreboard
        void displayScore() {
            // Step 1: Print Scoreboard Top Border
            System.out.println("\n======================================");

            // Step 2: Format Scoreboard Content
            String scoreText = "SCORE: " + player.name + " [ " + player.score
                    + " ] - System [ " + system.score + " ]";
            int pad = 36 - scoreText.length();
            int left = Math.max(pad / 2, 0);
            int right = Math.max(pad - left, 0);
            System.out.println("|" + " ".repeat(left) + scoreText + " ".repeat(right) + "|");

            // Step 3: Print Scoreboard Bottom Border
            System.out.println("======================================");
        }

        // Task 12 - Play a single round and reveal choices
        void playRound(int roundNum) {
            // Step 1: Print Round Header
            System.out.println("\n--- Round " + roundNum + " ---");

            // Step 2: Collect Opponent Moves
            String playerMove = player.chooseMove(scanner);
            String systemMove = system.chooseMove();

            // Step 3: Reveal Choices
            System.out.println("\n" + player.name + " chose: " + playerMove);
            System.out.println("System chose: " + systemMove);

            // Step 4: Evaluate Outcome
            RoundResult result = determineWinner(playerMove, systemMove);

            // Step 5: Update Scores and Announce Result
            if (result.winner.equals("draw")) {
                System.out.println("Result: It's a draw! (" + result.reason + ")");
            } else if (result.winner.equals("player")) {
                player.score++;
                System.out.println("Result: " + result.reason + "! " + player.name + " wins Round " + roundNum + "!");
            } else {
                system.score++;
                System.out.println("Result: " + result.reason + "! System wins Round " + roundNum + "!");
            }

            // Step 6: Refresh Scoreboard
            displayScore();
        }

        // Task 13 - Implement match champion announcement
        void announceChampion() {
            // Step 1: Print Match Finished Banner
            System.out.println("\n===== MATCH FINISHED =====");

            // Step 2: Evaluate Final Scores and Crown Champion
            if (player.score > system.score) {
                System.out.println("MATCH CHAMPION: " + player.name + " wins the match!");
            } else {
                System.out.println("MATCH CHAMPION: System wins the match! Better luck next time!");
            }
        }

        // Task 14 - Write the playMatch() loop
        void playMatch() {
            // Step 1: Reset Opponent Scores
            player.resetScore();
            system.resetScore();
            int roundNum = 1;

            // Step 2: Print Match Start Banner
            System.out.println("\n===== NEW MATCH STARTED =====");
            System.out.println("First to reach " + targetScore + " points wins the match!");

            // Step 3: Run Turn-Based Round Loop
            while (player.score < targetScore && system.score < targetScore) {
                playRound(roundNum);
                roundNum++;
            }

            // Step 4: Announce Match Champion
            announceChampion();
        }

        // Task 15 - Implement askReplay()
        static boolean askReplay(Scanner scanner) {
            // Step 1: Interactive Replay Prompt Loop
            while (true) {
                // Step 2: Read and Normalize Confirmation Input
                System.out.print("\nPlay again? (y/n): ");
                if (!scanner.hasNextLine()) return false;
                String answer = scanner.nextLine().trim().toLowerCase();

                // Step 3: Evaluate Replay Choice
                if (answer.equals("y")) return true;
                if (answer.equals("n")) return false;

                System.out.println("Please type y or n.");
            }
        }

        // Task 16 - Implement playMany() for continuous play
        void playMany() {
            // Step 1: Continuous Match Session Loop
            while (true) {
                // Step 2: Execute Match Lifecycle
                playMatch();

                // Step 3: Prompt for Rematch Confirmation
                if (!askReplay(scanner)) {
                    // Step 4: Display Session Farewell on Exit
                    System.out.println("\nThanks for playing Stone Paper Scissors!");
                    break;
                }
            }
        }
    }

    // Task 17 - Assemble the main() entry point
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Step 1: Initialize System Environment and Welcome Banner
        printWelcome();

        // Step 2: Capture Player Identity
        System.out.print("Enter your name: ");
        String playerName = scanner.nextLine();

        // Step 3: Instantiate Game Manager
        Game game = new Game(playerName, scanner);

        // Step 4: Launch Continuous Match Session
        game.playMany();
    }
}
