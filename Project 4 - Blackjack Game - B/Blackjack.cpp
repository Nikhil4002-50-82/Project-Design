// Task 1 - Create the entry file and print welcome message
// Step 1: Entry File Setup
#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <cctype>

using namespace std;

void printWelcome() {
    // Step 2: Welcome Banner Output
    cout << "Welcome to Blackjack!\n";
}

// Task 2 - Define standard ranks and suits constants
// Step 1: Declare Rank Collection
const vector<string> RANKS = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"};

// Step 2: Declare Suit Collection
const vector<string> SUITS = {"Hearts", "Diamonds", "Clubs", "Spades"};

// Task 3 - Create the Card class
struct Card {
    string rank;
    string suit;

    // Step 1: Initialize Card Rank and Suit
    Card(string r = "", string s = "") : rank(r), suit(s) {}

    // Step 2: Format Card Description
    string toString() const {
        return rank + " of " + suit;
    }
};

// Task 4 - Create and populate the 52-card deck
vector<Card> createDeck() {
    // Step 1: Initialize Empty Deck Collection
    vector<Card> deck;

    // Step 2: Populate Combinations with Nested Loops
    for (const string& suit : SUITS) {
        for (const string& rank : RANKS) {
            deck.push_back(Card(rank, suit));
        }
    }

    // Step 3: Return Completed Deck
    return deck;
}

// Task 5 - Shuffle the deck
void shuffleDeck(vector<Card>& deck) {
    // Step 1: Receive Deck Reference
    // Step 2: Randomize Card Positions in Place
    for (size_t i = 0; i < deck.size(); ++i) {
        int j = rand() % deck.size();
        swap(deck[i], deck[j]);
    }
}

// Task 6 - Deal a card from the deck
Card dealCard(vector<Card>& deck) {
    // Step 1: Extract Top Card from Collection
    Card topCard = deck.back();
    deck.pop_back();

    // Step 2: Return Dealt Card
    return topCard;
}

// Task 7 - Calculate hand value with automatic Ace adjustment
int calculateScore(const vector<Card>& hand) {
    // Step 1: Initialize Point Accumulator and Ace Counter
    int total = 0;
    int aceCount = 0;

    // Step 2: Accumulate Card Values and Count Aces
    for (const Card& card : hand) {
        if (card.rank == "Jack" || card.rank == "Queen" || card.rank == "King") {
            total += 10;
        } else if (card.rank == "Ace") {
            total += 11;
            aceCount++;
        } else {
            total += stoi(card.rank);
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
void displayHand(const string& ownerName, const vector<Card>& hand, bool hideFirstCard = false) {
    // Step 1: Check Hole Card Masking Flag
    if (hideFirstCard) {
        // Step 2: Render Masked Hand for Dealer
        cout << ownerName << "'s Hand: [Hidden Card], " << hand[1].toString() << "\n";
    } else {
        // Step 3: Render Formatted Visible Hand with Score
        cout << ownerName << "'s Hand (" << calculateScore(hand) << "): ";
        for (size_t i = 0; i < hand.size(); ++i) {
            cout << hand[i].toString();
            if (i + 1 < hand.size()) {
                cout << ", ";
            }
        }
        cout << "\n";
    }
}

// Task 9 - Prompt and validate Player choice (Hit or Stand)
char getPlayerChoice() {
    // Step 1: Interactive Input Prompt Loop
    while (true) {
        cout << "\nWould you like to (H)it or (S)tand? ";
        string input;
        getline(cin, input);

        // Step 2: Clean and Normalize Input
        size_t start = input.find_first_not_of(" \t\r\n");
        size_t end = input.find_last_not_of(" \t\r\n");
        string cleaned = (start == string::npos) ? "" : input.substr(start, end - start + 1);
        for (char& ch : cleaned) {
            ch = static_cast<char>(tolower(static_cast<unsigned char>(ch)));
        }

        // Step 3: Evaluate Valid Choice or Re-prompt
        if (cleaned == "h" || cleaned == "hit") {
            return 'h';
        } else if (cleaned == "s" || cleaned == "stand") {
            return 's';
        } else {
            cout << "Invalid input. Please enter 'h' to hit or 's' to stand.\n";
        }
    }
}

// Task 10 - Execute Dealer's automated turn
void playDealerTurn(vector<Card>& deck, vector<Card>& dealerHand) {
    // Step 1: Announce Dealer Turn and Reveal Hole Card
    cout << "\n--- Dealer's Turn ---\n";
    displayHand("Dealer", dealerHand, false);

    // Step 2: Automated Hit Loop While Score Under 17
    while (calculateScore(dealerHand) < 17) {
        // Step 3: Draw Card, Announce Draw, and Refresh Display
        Card card = dealCard(deck);
        dealerHand.push_back(card);
        cout << "Dealer hits and draws: " << card.toString() << "\n";
        displayHand("Dealer", dealerHand, false);
    }

    // Step 4: Evaluate and Announce Dealer Stand or Bust
    int score = calculateScore(dealerHand);
    if (score > 21) {
        cout << "Dealer busted!\n";
    } else {
        cout << "Dealer stands with " << score << ".\n";
    }
}

// Task 11 - Determine and announce round outcome
string determineOutcome(const vector<Card>& playerHand, const vector<Card>& dealerHand) {
    // Step 1: Calculate Final Scores and Display Matchup Summary
    int playerScore = calculateScore(playerHand);
    int dealerScore = calculateScore(dealerHand);

    cout << "\n===== ROUND RESULT =====\n";
    displayHand("Player", playerHand, false);
    displayHand("Dealer", dealerHand, false);

    // Step 2: Check Player Bust Condition
    if (playerScore > 21) {
        cout << "\nDealer wins! You went over 21.\n";
        return "dealer";
    }
    // Step 3: Check Dealer Bust Condition
    else if (dealerScore > 21) {
        cout << "\nYou win! Dealer went over 21.\n";
        return "player";
    }
    // Step 4: Compare Final Hand Scores and Announce Result
    else if (playerScore > dealerScore) {
        cout << "\nYou win! Your " << playerScore << " beats Dealer's " << dealerScore << ".\n";
        return "player";
    } else if (dealerScore > playerScore) {
        cout << "\nDealer wins! Dealer's " << dealerScore << " beats your " << playerScore << ".\n";
        return "dealer";
    } else {
        // Step 5: Return Standard Outcome Identifier
        cout << "\nIt's a push (tie)! Both have " << playerScore << ".\n";
        return "tie";
    }
}

// Task 12 - Manage and display session scoreboard
void displayScoreboard(int playerWins, int dealerWins, int ties) {
    // Step 1: Format Scoreboard Card Border
    cout << "\n------------------------------------\n";
    // Step 2: Print Cumulative Tally Line
    cout << "SCOREBOARD: Player: " << playerWins << " | Dealer: " << dealerWins << " | Ties: " << ties << "\n";
    cout << "------------------------------------\n";
}

// Task 13 - Create BlackjackGame class and implement playRound()
class BlackjackGame {
public:
    int playerWins;
    int dealerWins;
    int ties;

    BlackjackGame() {
        // Step 1: Initialize Session Score Counters
        playerWins = 0;
        dealerWins = 0;
        ties = 0;
    }

    void updateScores(const string& outcome) {
        if (outcome == "player") {
            playerWins++;
        } else if (outcome == "dealer") {
            dealerWins++;
        } else if (outcome == "tie") {
            ties++;
        }
        displayScoreboard(playerWins, dealerWins, ties);
    }

    void playRound() {
        // Step 2: Generate, Shuffle, and Deal Opening Cards
        vector<Card> deck = createDeck();
        shuffleDeck(deck);

        vector<Card> playerHand = {dealCard(deck), dealCard(deck)};
        vector<Card> dealerHand = {dealCard(deck), dealCard(deck)};

        // Step 3: Render Opening Hands with Dealer Hole Card Masked
        cout << "\n===== NEW BLACKJACK ROUND =====\n";
        displayHand("Dealer", dealerHand, true);
        displayHand("Player", playerHand, false);

        // Step 4: Check Natural Opening Blackjack
        if (calculateScore(playerHand) == 21) {
            cout << "\nBlackjack! You have 21!\n";
            string outcome = determineOutcome(playerHand, dealerHand);
            updateScores(outcome);
            return;
        }

        // Step 5: Execute Interactive Player Turn Loop
        while (calculateScore(playerHand) < 21) {
            char choice = getPlayerChoice();
            if (choice == 'h') {
                Card card = dealCard(deck);
                playerHand.push_back(card);
                cout << "\nYou drew: " << card.toString() << "\n";
                displayHand("Player", playerHand, false);
            } else {
                cout << "\nYou chose to stand.\n";
                break;
            }
        }

        if (calculateScore(playerHand) > 21) {
            cout << "\nYou busted with " << calculateScore(playerHand) << "!\n";
            string outcome = determineOutcome(playerHand, dealerHand);
            updateScores(outcome);
            return;
        }

        // Step 6: Execute Dealer Turn and Resolve Outcome
        playDealerTurn(deck, dealerHand);
        string outcome = determineOutcome(playerHand, dealerHand);
        updateScores(outcome);
    }

    // Task 14 - Implement askReplay()
    static bool askReplay() {
        // Step 1: Interactive Rematch Confirmation Loop
        while (true) {
            cout << "\nPlay another round? (y/n): ";
            string input;
            getline(cin, input);

            // Step 2: Normalize Input and Return Decision
            size_t start = input.find_first_not_of(" \t\r\n");
            size_t end = input.find_last_not_of(" \t\r\n");
            string cleaned = (start == string::npos) ? "" : input.substr(start, end - start + 1);
            for (char& ch : cleaned) {
                ch = static_cast<char>(tolower(static_cast<unsigned char>(ch)));
            }

            if (cleaned == "y" || cleaned == "yes") {
                return true;
            } else if (cleaned == "n" || cleaned == "no") {
                return false;
            } else {
                cout << "Please enter 'y' for yes or 'n' for no.\n";
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
                cout << "\nFinal Session Stats:\n";
                displayScoreboard(playerWins, dealerWins, ties);
                cout << "Thanks for playing Blackjack!\n";
                break;
            }
        }
    }
};

// Task 16 - Assemble the main() entry point
int main() {
    srand(static_cast<unsigned int>(time(nullptr)));

    // Step 1: Instantiate Game Manager
    BlackjackGame game;

    // Step 2: Launch Continuous Session
    game.playMany();

    return 0;
}
