// Task 1 - Create the entry file and print welcome message
// Step 1: Entry File Setup
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Blackjack {

    static Scanner scanner = new Scanner(System.in);

    static void printWelcome() {
        // Step 2: Welcome Banner Output
        System.out.println("Welcome to Blackjack!");
    }

    // Task 2 - Define standard ranks and suits constants
    // Step 1: Declare Rank Collection
    static final String[] RANKS = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"};

    // Step 2: Declare Suit Collection
    static final String[] SUITS = {"Hearts", "Diamonds", "Clubs", "Spades"};

    // Task 3 - Create the Card class
    static class Card {
        String rank;
        String suit;

        // Step 1: Initialize Card Rank and Suit
        Card(String rank, String suit) {
            this.rank = rank;
            this.suit = suit;
        }

        // Step 2: Format Card Description
        @Override
        public String toString() {
            return rank + " of " + suit;
        }
    }

    // Task 4 - Create and populate the 52-card deck
    static List<Card> createDeck() {
        // Step 1: Initialize Empty Deck Collection
        List<Card> deck = new ArrayList<>();

        // Step 2: Populate Combinations with Nested Loops
        for (String suit : SUITS) {
            for (String rank : RANKS) {
                deck.add(new Card(rank, suit));
            }
        }

        // Step 3: Return Completed Deck
        return deck;
    }

    // Task 5 - Shuffle the deck
    static void shuffleDeck(List<Card> deck) {
        // Step 1: Receive Deck Reference
        // Step 2: Randomize Card Positions in Place
        Collections.shuffle(deck);
    }

    // Task 6 - Deal a card from the deck
    static Card dealCard(List<Card> deck) {
        // Step 1: Extract Top Card from Collection
        // Step 2: Return Dealt Card
        return deck.remove(deck.size() - 1);
    }

    // Task 7 - Calculate hand value with automatic Ace adjustment
    static int calculateScore(List<Card> hand) {
        // Step 1: Initialize Point Accumulator and Ace Counter
        int total = 0;
        int aceCount = 0;

        // Step 2: Accumulate Card Values and Count Aces
        for (Card card : hand) {
            if (card.rank.equals("Jack") || card.rank.equals("Queen") || card.rank.equals("King")) {
                total += 10;
            } else if (card.rank.equals("Ace")) {
                total += 11;
                aceCount++;
            } else {
                total += Integer.parseInt(card.rank);
            }
        }

        // Step 3: Dynamically Downgrade Aces to Avoid Busting
        while (total > 21 && aceCount > 0) {
            total -= 10;
            aceCount--;
        }

        // Step 4: Return Calculated Hand Score
        return total;
    }

    // Task 8 - Display hands with hidden hole card support
    static void displayHand(String ownerName, List<Card> hand, boolean hideFirstCard) {
        // Step 1: Check Hole Card Masking Flag
        if (hideFirstCard) {
            // Step 2: Render Masked Hand for Dealer
            System.out.println(ownerName + "'s Hand: [Hidden Card], " + hand.get(1));
        } else {
            // Step 3: Render Formatted Visible Hand with Score
            List<String> cardNames = new ArrayList<>();
            for (Card card : hand) {
                cardNames.add(card.toString());
            }
            int score = calculateScore(hand);
            System.out.println(ownerName + "'s Hand (" + score + "): " + String.join(", ", cardNames));
        }
    }

    // Task 9 - Prompt and validate Player choice (Hit or Stand)
    static char getPlayerChoice() {
        // Step 1: Interactive Input Prompt Loop
        while (true) {
            System.out.print("\nWould you like to (H)it or (S)tand? ");
            String input = scanner.nextLine().trim().toLowerCase();

            // Step 2: Clean and Normalize Input
            // Step 3: Evaluate Valid Choice or Re-prompt
            if (input.equals("h") || input.equals("hit")) {
                return 'h';
            } else if (input.equals("s") || input.equals("stand")) {
                return 's';
            } else {
                System.out.println("Invalid input. Please enter 'h' to hit or 's' to stand.");
            }
        }
    }

    // Task 10 - Execute Dealer's automated turn
    static void playDealerTurn(List<Card> deck, List<Card> dealerHand) {
        // Step 1: Announce Dealer Turn and Reveal Hole Card
        System.out.println("\n--- Dealer's Turn ---");
        displayHand("Dealer", dealerHand, false);

        // Step 2: Automated Hit Loop While Score Under 17
        while (calculateScore(dealerHand) < 17) {
            // Step 3: Draw Card, Announce Draw, and Refresh Display
            Card card = dealCard(deck);
            dealerHand.add(card);
            System.out.println("Dealer hits and draws: " + card);
            displayHand("Dealer", dealerHand, false);
        }

        // Step 4: Evaluate and Announce Dealer Stand or Bust
        int score = calculateScore(dealerHand);
        if (score > 21) {
            System.out.println("Dealer busted!");
        } else {
            System.out.println("Dealer stands with " + score + ".");
        }
    }

    // Task 11 - Determine and announce round outcome
    static String determineOutcome(List<Card> playerHand, List<Card> dealerHand) {
        // Step 1: Calculate Final Scores and Display Matchup Summary
        int playerScore = calculateScore(playerHand);
        int dealerScore = calculateScore(dealerHand);

        System.out.println("\n===== ROUND RESULT =====");
        displayHand("Player", playerHand, false);
        displayHand("Dealer", dealerHand, false);

        // Step 2: Check Player Bust Condition
        if (playerScore > 21) {
            System.out.println("\nDealer wins! You went over 21.");
            return "dealer";
        }
        // Step 3: Check Dealer Bust Condition
        else if (dealerScore > 21) {
            System.out.println("\nYou win! Dealer went over 21.");
            return "player";
        }
        // Step 4: Compare Final Hand Scores and Announce Result
        else if (playerScore > dealerScore) {
            System.out.println("\nYou win! Your " + playerScore + " beats Dealer's " + dealerScore + ".");
            return "player";
        } else if (dealerScore > playerScore) {
            System.out.println("\nDealer wins! Dealer's " + dealerScore + " beats your " + playerScore + ".");
            return "dealer";
        } else {
            // Step 5: Return Standard Outcome Identifier
            System.out.println("\nIt's a push (tie)! Both have " + playerScore + ".");
            return "tie";
        }
    }

    // Task 12 - Manage and display session scoreboard
    static void displayScoreboard(int playerWins, int dealerWins, int ties) {
        // Step 1: Format Scoreboard Card Border
        System.out.println("\n------------------------------------");
        // Step 2: Print Cumulative Tally Line
        System.out.println("SCOREBOARD: Player: " + playerWins + " | Dealer: " + dealerWins + " | Ties: " + ties);
        System.out.println("------------------------------------");
    }

    // Task 13 - Create BlackjackGame class and implement playRound()
    static class BlackjackGame {
        int playerWins;
        int dealerWins;
        int ties;

        BlackjackGame() {
            // Step 1: Initialize Session Score Counters
            playerWins = 0;
            dealerWins = 0;
            ties = 0;
        }

        void updateScores(String outcome) {
            if (outcome.equals("player")) {
                playerWins++;
            } else if (outcome.equals("dealer")) {
                dealerWins++;
            } else if (outcome.equals("tie")) {
                ties++;
            }
            displayScoreboard(playerWins, dealerWins, ties);
        }

        void playRound() {
            // Step 2: Generate, Shuffle, and Deal Opening Cards
            List<Card> deck = createDeck();
            shuffleDeck(deck);

            List<Card> playerHand = new ArrayList<>();
            playerHand.add(dealCard(deck));
            playerHand.add(dealCard(deck));

            List<Card> dealerHand = new ArrayList<>();
            dealerHand.add(dealCard(deck));
            dealerHand.add(dealCard(deck));

            // Step 3: Render Opening Hands with Dealer Hole Card Masked
            System.out.println("\n===== NEW BLACKJACK ROUND =====");
            displayHand("Dealer", dealerHand, true);
            displayHand("Player", playerHand, false);

            // Step 4: Check Natural Opening Blackjack
            if (calculateScore(playerHand) == 21) {
                System.out.println("\nBlackjack! You have 21!");
                String outcome = determineOutcome(playerHand, dealerHand);
                updateScores(outcome);
                return;
            }

            // Step 5: Execute Interactive Player Turn Loop
            while (calculateScore(playerHand) < 21) {
                char choice = getPlayerChoice();
                if (choice == 'h') {
                    Card card = dealCard(deck);
                    playerHand.add(card);
                    System.out.println("\nYou drew: " + card);
                    displayHand("Player", playerHand, false);
                } else {
                    System.out.println("\nYou chose to stand.");
                    break;
                }
            }

            if (calculateScore(playerHand) > 21) {
                System.out.println("\nYou busted with " + calculateScore(playerHand) + "!");
                String outcome = determineOutcome(playerHand, dealerHand);
                updateScores(outcome);
                return;
            }

            // Step 6: Execute Dealer Turn and Resolve Outcome
            playDealerTurn(deck, dealerHand);
            String outcome = determineOutcome(playerHand, dealerHand);
            updateScores(outcome);
        }

        // Task 14 - Implement askReplay()
        static boolean askReplay() {
            // Step 1: Interactive Rematch Confirmation Loop
            while (true) {
                System.out.print("\nPlay another round? (y/n): ");
                String input = scanner.nextLine().trim().toLowerCase();

                // Step 2: Normalize Input and Return Decision
                if (input.equals("y") || input.equals("yes")) {
                    return true;
                } else if (input.equals("n") || input.equals("no")) {
                    return false;
                } else {
                    System.out.println("Please enter 'y' for yes or 'n' for no.");
                }
            }
        }

        // Task 15 - Implement playMany() for continuous play
        void playMany() {
            // Step 1: Display Welcome Greeting
            printWelcome();

            // Step 2: Continuous Round Execution Loop
            while (true) {
                playRound();

                // Step 3: Prompt Replay and Present Final Session Stats on Exit
                if (!askReplay()) {
                    System.out.println("\nFinal Session Stats:");
                    displayScoreboard(playerWins, dealerWins, ties);
                    System.out.println("Thanks for playing Blackjack!");
                    break;
                }
            }
        }
    }

    // Task 16 - Assemble the main() entry point
    public static void main(String[] args) {
        // Step 1: Instantiate Game Manager
        BlackjackGame game = new BlackjackGame();

        // Step 2: Launch Continuous Session
        game.playMany();
    }
}
