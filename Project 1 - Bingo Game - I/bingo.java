import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

class Bingo {

    // Task 1 - Create the entry file and print welcome message
    // Step 1: Entry File Setup
    // Step 2: Welcome Banner Output
    static void printWelcome() {
        System.out.println("Welcome to Bingo!");
    }

    // Task 2 - Define the 12 winning lines and FREE center index
    // Step 1: Center Index Constant
    static final int FREE_INDEX = 12;

    // Step 2: Winning Lines Matrix
    static final int[][] WIN_LINES = {
        {0, 1, 2, 3, 4}, {5, 6, 7, 8, 9}, {10, 11, 12, 13, 14},        // rows
        {15, 16, 17, 18, 19}, {20, 21, 22, 23, 24},
        {0, 5, 10, 15, 20}, {1, 6, 11, 16, 21}, {2, 7, 12, 17, 22},    // columns
        {3, 8, 13, 18, 23}, {4, 9, 14, 19, 24},
        {0, 6, 12, 18, 24}, {4, 8, 12, 16, 20},                        // diagonals
    };

    // Task 3 - Create the Card class and generate numbers
    static class Card {
        int[] numbers = new int[25];
        boolean[] marked = new boolean[25];

        Card() {
            // Step 1: State Initialization
            generate();
            marked[FREE_INDEX] = true;
        }

        void generate() {
            int[] low  = {1, 16, 31, 46, 61};
            int[] high = {15, 30, 45, 60, 75};

            // Step 2: Column-Wise Number Generation
            for (int col = 0; col < 5; col++) {
                List<Integer> colNumbers = new ArrayList<>();
                for (int v = low[col]; v <= high[col]; v++) colNumbers.add(v);
                Collections.shuffle(colNumbers);
                // Step 3: 1D Grid Coordinate Mapping & Center FREE Placement
                for (int row = 0; row < 5; row++) {
                    numbers[row * 5 + col] = colNumbers.get(row);
                }
            }
            numbers[FREE_INDEX] = -1;
        }

        // Task 4 - Display the card
        void display(String title) {
            // Step 1: Header Title & Row Iteration
            System.out.println("\n" + title);
            for (int row = 0; row < 5; row++) {
                StringBuilder line = new StringBuilder();
                // Step 2: Cell Formatting & Daub Indicator
                for (int col = 0; col < 5; col++) {
                    int idx = row * 5 + col;
                    String text = (numbers[idx] == -1) ? "FREE" : String.valueOf(numbers[idx]);
                    if (marked[idx]) text = "*" + text + "*";
                    line.append(center(text, 6));
                    if (col != 4) line.append("|");
                }
                // Step 3: Pipe Separators & Horizontal Dividers
                System.out.println(line);
                if (row != 4) System.out.println("-".repeat(34));
            }
        }

        private static String center(String text, int width) {
            int pad = width - text.length();
            int left = pad / 2, right = pad - left;
            return " ".repeat(Math.max(left, 0)) + text + " ".repeat(Math.max(right, 0));
        }

        // Task 5 - Implement mark(number)
        boolean mark(int number) {
            // Step 1: Linear Search for Target Value
            for (int i = 0; i < 25; i++) {
                // Step 2: Daub & Confirmation Return
                if (numbers[i] == number && !marked[i]) {
                    marked[i] = true;
                    return true;
                }
            }
            return false;
        }

        // Task 6 - Implement checkWin()
        boolean checkWin() {
            // Step 1: Iterate Winning Line Definitions
            for (int[] line : WIN_LINES) {
                // Step 2: Line Verification & Early Exit
                boolean lineComplete = true;
                for (int idx : line) {
                    if (!marked[idx]) {
                        lineComplete = false;
                        break;
                    }
                }
                if (lineComplete) return true;
            }
            return false;
        }
    }

    // Task 7 - Create the Player class
    static class Player {
        String name;
        Card card;
        boolean hasWon = false;

        Player(String rawName) {
            // Step 1: Name Sanitization & Default Assignment
            if (rawName != null && !rawName.trim().isEmpty()) {
                this.name = rawName.trim();
            } else {
                this.name = "Player";
            }
            // Step 2: Card Ownership & Victory Flag
            this.card = new Card();
        }
    }

    // Task 8 - Build a list of players
    static List<Player> buildPlayers(Scanner scanner) {
        // Step 1: Player Count Prompt & Defensive Validation
        int numPlayers = 0;
        while (true) {
            System.out.print("How many players (1-6)? ");
            String userInput = scanner.nextLine().trim();
            boolean allDigits = !userInput.isEmpty();
            for (int j = 0; j < userInput.length(); j++) {
                if (!Character.isDigit(userInput.charAt(j))) {
                    allDigits = false;
                    break;
                }
            }
            if (allDigits) {
                numPlayers = Integer.parseInt(userInput);
                if (numPlayers >= 1 && numPlayers <= 6) break;
            }
            System.out.println("Please enter a number from 1 to 6.");
        }

        // Step 2: Roster Instantiation Loop
        List<Player> players = new ArrayList<>();
        for (int i = 1; i <= numPlayers; i++) {
            System.out.print("Enter name for Player " + i + ": ");
            String name = scanner.nextLine();
            players.add(new Player(name));
        }
        return players;
    }

    // Task 9 - Create the Game class skeleton
    static class Game {
        List<Player> players;
        List<Integer> numberPool = new ArrayList<>();
        List<Integer> calledNumbers = new ArrayList<>();
        Scanner scanner;

        Game(List<Player> players, Scanner scanner) {
            // Step 1: State Binding
            this.players = players;
            this.scanner = scanner;
            // Step 2: Number Pool Generation & Shuffling
            resetNumberPool();
        }

        void resetNumberPool() {
            numberPool.clear();
            for (int v = 1; v <= 75; v++) numberPool.add(v);
            Collections.shuffle(numberPool);
            calledNumbers.clear();
        }

        // Task 10 - Implement drawNumber()
        int drawNumber() {
            // Step 1: Draw from Pool
            int number = numberPool.remove(numberPool.size() - 1);
            // Step 2: History Logging & Return
            calledNumbers.add(number);
            return number;
        }

        // Task 11 - Broadcast a drawn number to every player
        void broadcast(int number) {
            // Step 1: Roster Broadcast Loop
            for (Player player : players) {
                // Step 2: Console Daub Notification
                if (player.card.mark(number)) {
                    System.out.println("  -> marked on " + player.name + "'s card");
                }
            }
        }

        // Task 12 - Check every player for a win, every round
        List<Player> checkWinners() {
            // Step 1: Winner Collection Scan
            List<Player> winners = new ArrayList<>();
            for (Player player : players) {
                // Step 2: Flag State & Winner Accumulation
                if (player.card.checkWin()) {
                    player.hasWon = true;
                    winners.add(player);
                }
            }
            return winners;
        }

        // Task 13 - Write the interactive play() loop
        void play() {
            // Step 1: Match Setup & Card Reveal
            resetNumberPool();
            for (Player player : players) {
                player.hasWon = false;
                player.card = new Card();
                System.out.print("\n" + player.name + ", press Enter to draw your card:");
                scanner.nextLine();
                player.card.display(player.name + "'s Card");
            }

            // Step 2: Match Start Indicator & Status Tracking
            System.out.println("\n===== MATCH STARTED =====");
            List<Player> winners = new ArrayList<>();
            int turn = 0;

            // Step 3: Turn-Based Draw Loop & Interactive Pacing
            while (!numberPool.isEmpty() && winners.isEmpty()) {
                Player activePlayer = players.get(turn % players.size());
                System.out.print("\n" + activePlayer.name + ", press Enter to draw the next number:");
                scanner.nextLine();

                int number = drawNumber();
                System.out.println("\nNumber called: " + number
                        + "  (draw #" + calledNumbers.size() + ")");

                // Step 4: Broadcast, Win Check & Turn Increment
                broadcast(number);
                winners = checkWinners();
                turn++;
            }

            // Step 5: Match Conclusion Dispatch
            announceResult(winners);
        }

        // Task 14 - Announce the result
        void announceResult(List<Player> winners) {
            // Step 1: Branch on Win vs. Draw
            if (!winners.isEmpty()) {
                // Step 2: Winner Showcase & Final Card Grid Display
                for (Player player : players) {
                    player.card.display(player.name + "'s Final Card");
                }
                StringBuilder names = new StringBuilder();
                for (int i = 0; i < winners.size(); i++) {
                    names.append(winners.get(i).name);
                    if (i + 1 != winners.size()) names.append(", ");
                }
                System.out.println("\nBINGO! " + names + " won after "
                        + calledNumbers.size() + " numbers called!");
            } else {
                // Step 3: Exhausted Pool Draw Message
                System.out.println("\nAll 75 numbers were called with no winner. It's a draw!");
            }
        }

        // Task 15 - Implement askReplay()
        static boolean askReplay(Scanner scanner) {
            // Step 1: Interactive Loop & Choice Prompt
            while (true) {
                System.out.print("Play again? (y/n): ");
                String answer = scanner.nextLine().trim().toLowerCase();
                // Step 2: Sanitization & Normalized Matching
                if (answer.equals("y")) return true;
                if (answer.equals("n")) return false;
                System.out.println("Please type y or n.");
            }
        }

        // Task 16 - Implement playMany()
        void playMany() {
            // Step 1: Multi-Match Indefinite Loop
            while (true) {
                play();
                // Step 2: Rematch Evaluation & Exit Farewell
                if (!askReplay(scanner)) {
                    System.out.println("Thanks for playing Bingo!");
                    break;
                }
            }
        }
    }

    // Task 17 - Assemble the main() entry point
    public static void main(String[] args) {
        // Step 1: Component Initialization Pipeline
        printWelcome();
        Scanner scanner = new Scanner(System.in);
        List<Player> players = buildPlayers(scanner);
        Game game = new Game(players, scanner);
        // Step 2: Kickoff Application Session
        game.playMany();
    }
}