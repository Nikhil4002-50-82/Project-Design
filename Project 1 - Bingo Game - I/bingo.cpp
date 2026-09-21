#include <algorithm>
#include <iostream>
#include <random>
#include <string>
#include <vector>

using namespace std;

// Task 1 - Create the entry file and print welcome message
// Step 1: Entry File Setup
// Step 2: Welcome Banner Output
void printWelcome() {
    cout << "Welcome to Bingo!\n";
}

// Task 2 - Define the 12 winning lines and FREE center index
// Step 1: Center Index Constant
const int FREE_INDEX = 12;

// Step 2: Winning Lines Matrix
static const vector<vector<int>> WIN_LINES = {
    {0, 1, 2, 3, 4}, {5, 6, 7, 8, 9}, {10, 11, 12, 13, 14},        // rows
    {15, 16, 17, 18, 19}, {20, 21, 22, 23, 24},
    {0, 5, 10, 15, 20}, {1, 6, 11, 16, 21}, {2, 7, 12, 17, 22},    // columns
    {3, 8, 13, 18, 23}, {4, 9, 14, 19, 24},
    {0, 6, 12, 18, 24}, {4, 8, 12, 16, 20},                        // diagonals
};

// Random number engine for shuffling
static mt19937 rng(random_device{}());

// Helper function to center text within a given column width
string center(const string& text, int width) {
    int pad = width - static_cast<int>(text.size());
    int left = pad / 2;
    int right = pad - left;
    return string(left > 0 ? left : 0, ' ') + text + string(right > 0 ? right : 0, ' ');
}

// Task 3 - Create the Card class and generate numbers
class Card {
public:
    vector<int> numbers;   // -1 marks the FREE cell
    vector<bool> marked;

    Card() : numbers(25), marked(25, false) {
        // Step 1: State Initialization
        generate();
        marked[FREE_INDEX] = true;
    }

    void generate() {
        int low[5]  = {1, 16, 31, 46, 61};
        int high[5] = {15, 30, 45, 60, 75};

        // Step 2: Column-Wise Number Generation
        for (int col = 0; col < 5; ++col) {
            vector<int> colNumbers;
            for (int v = low[col]; v <= high[col]; ++v) {
                colNumbers.push_back(v);
            }
            shuffle(colNumbers.begin(), colNumbers.end(), rng);
            // Step 3: 1D Grid Coordinate Mapping & Center FREE Placement
            for (int row = 0; row < 5; ++row) {
                numbers[row * 5 + col] = colNumbers[row];
            }
        }
        numbers[FREE_INDEX] = -1;
    }

    // Task 4 - Display the card
    void display(const string& title) const {
        // Step 1: Header Title & Row Iteration
        cout << "\n" << title << "\n";
        for (int row = 0; row < 5; ++row) {
            string line = "";
            // Step 2: Cell Formatting & Daub Indicator
            for (int col = 0; col < 5; ++col) {
                int idx = row * 5 + col;
                string text = (numbers[idx] == -1) ? "FREE" : to_string(numbers[idx]);
                if (marked[idx]) text = "*" + text + "*";
                line += center(text, 6);
                if (col != 4) line += "|";
            }
            // Step 3: Pipe Separators & Horizontal Dividers
            cout << line << "\n";
            if (row != 4) cout << string(34, '-') << "\n";
        }
    }

    // Task 5 - Implement mark(number)
    bool mark(int number) {
        // Step 1: Linear Search for Target Value
        for (int i = 0; i < 25; ++i) {
            // Step 2: Daub & Confirmation Return
            if (numbers[i] == number && !marked[i]) {
                marked[i] = true;
                return true;
            }
        }
        return false;
    }

    // Task 6 - Implement checkWin()
    bool checkWin() const {
        // Step 1: Iterate Winning Line Definitions
        for (const auto& line : WIN_LINES) {
            // Step 2: Line Verification & Early Exit
            bool lineComplete = true;
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
};

// Task 7 - Create the Player class
class Player {
public:
    string name;
    Card card;
    bool hasWon = false;

    explicit Player(const string& rawName) {
        // Step 1: Name Sanitization & Default Assignment
        size_t start = 0;
        while (start < rawName.size() && (rawName[start] == ' ' || rawName[start] == '\t')) {
            start++;
        }
        if (start == rawName.size()) {
            name = "Player";
        } else {
            name = rawName.substr(start);
        }
        // Step 2: Card Ownership & Victory Flag
        card = Card();
        hasWon = false;
    }
};

// Task 8 - Build a list of players
vector<Player> buildPlayers() {
    // Step 1: Player Count Prompt & Defensive Validation
    int numPlayers = 0;
    while (true) {
        cout << "How many players (1-6)? ";
        string userInput;
        getline(cin, userInput);
        bool allDigits = !userInput.empty();
        for (char c : userInput) {
            if (!isdigit(c)) {
                allDigits = false;
                break;
            }
        }
        if (allDigits) {
            numPlayers = stoi(userInput);
            if (numPlayers >= 1 && numPlayers <= 6) break;
        }
        cout << "Please enter a number from 1 to 6.\n";
    }

    // Step 2: Roster Instantiation Loop
    vector<Player> players;
    for (int i = 1; i <= numPlayers; ++i) {
        cout << "Enter name for Player " << i << ": ";
        string name;
        getline(cin, name);
        players.push_back(Player(name));
    }
    return players;
}

// Task 9 - Create the Game class skeleton
class Game {
public:
    vector<Player>& players;
    vector<int> numberPool;
    vector<int> calledNumbers;

    explicit Game(vector<Player>& players) : players(players) {
        // Step 1: State Binding
        // Step 2: Number Pool Generation & Shuffling
        resetNumberPool();
    }

    void resetNumberPool() {
        numberPool.clear();
        for (int v = 1; v <= 75; ++v) {
            numberPool.push_back(v);
        }
        shuffle(numberPool.begin(), numberPool.end(), rng);
        calledNumbers.clear();
    }

    // Task 10 - Implement drawNumber()
    int drawNumber() {
        // Step 1: Draw from Pool
        int number = numberPool.back();
        numberPool.pop_back();
        // Step 2: History Logging & Return
        calledNumbers.push_back(number);
        return number;
    }

    // Task 11 - Broadcast a drawn number to every player
    void broadcast(int number) {
        // Step 1: Roster Broadcast Loop
        for (auto& player : players) {
            // Step 2: Console Daub Notification
            if (player.card.mark(number)) {
                cout << "  -> marked on " << player.name << "'s card\n";
            }
        }
    }

    // Task 12 - Check every player for a win, every round
    vector<string> checkWinners() {
        // Step 1: Winner Collection Scan
        vector<string> winners;
        for (auto& player : players) {
            // Step 2: Flag State & Winner Accumulation
            if (player.card.checkWin()) {
                player.hasWon = true;
                winners.push_back(player.name);
            }
        }
        return winners;
    }

    // Task 13 - Write the interactive play() loop
    void play() {
        // Step 1: Match Setup & Card Reveal
        resetNumberPool();
        for (auto& player : players) {
            player.hasWon = false;
            player.card = Card();
            cout << "\n" << player.name << ", press Enter to draw your card:";
            string enterKey;
            getline(cin, enterKey);
            player.card.display(player.name + "'s Card");
        }

        // Step 2: Match Start Indicator & Status Tracking
        cout << "\n===== MATCH STARTED =====\n";
        vector<string> winners;
        size_t turn = 0;

        // Step 3: Turn-Based Draw Loop & Interactive Pacing
        while (!numberPool.empty() && winners.empty()) {
            Player& activePlayer = players[turn % players.size()];
            cout << "\n" << activePlayer.name << ", press Enter to draw the next number:";
            string enterKey;
            getline(cin, enterKey);

            int number = drawNumber();
            cout << "\nNumber called: " << number
                 << "  (draw #" << calledNumbers.size() << ")\n";

            // Step 4: Broadcast, Win Check & Turn Increment
            broadcast(number);
            winners = checkWinners();
            turn++;
        }

        // Step 5: Match Conclusion Dispatch
        announceResult(winners);
    }

    // Task 14 - Announce the result
    void announceResult(const vector<string>& winners) {
        // Step 1: Branch on Win vs. Draw
        if (!winners.empty()) {
            // Step 2: Winner Showcase & Final Card Grid Display
            for (auto& player : players) {
                player.card.display(player.name + "'s Final Card");
            }
            cout << "\nBINGO! ";
            for (size_t i = 0; i < winners.size(); ++i) {
                cout << winners[i];
                if (i + 1 != winners.size()) cout << ", ";
            }
            cout << " won after " << calledNumbers.size()
                 << " numbers called!\n";
        } else {
            // Step 3: Exhausted Pool Draw Message
            cout << "\nAll 75 numbers were called with no winner. It's a draw!\n";
        }
    }

    // Task 15 - Implement askReplay()
    static bool askReplay() {
        // Step 1: Interactive Loop & Choice Prompt
        while (true) {
            cout << "Play again? (y/n): ";
            string answer;
            getline(cin, answer);
            // Step 2: Sanitization & Normalized Matching
            if (answer == "y") return true;
            if (answer == "n") return false;
            cout << "Please type y or n.\n";
        }
    }

    // Task 16 - Implement playMany()
    void playMany() {
        // Step 1: Multi-Match Indefinite Loop
        while (true) {
            play();
            // Step 2: Rematch Evaluation & Exit Farewell
            if (!askReplay()) {
                cout << "Thanks for playing Bingo!\n";
                break;
            }
        }
    }
};

// Task 17 - Assemble the main() entry point
int main() {
    // Step 1: Component Initialization Pipeline
    printWelcome();
    vector<Player> players = buildPlayers();
    Game game(players);
    // Step 2: Kickoff Application Session
    game.playMany();
    return 0;
}