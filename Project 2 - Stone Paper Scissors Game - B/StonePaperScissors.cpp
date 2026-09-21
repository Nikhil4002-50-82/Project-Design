// Task 1 - Create the entry file and print welcome message
// Step 1: Entry File Setup
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void printWelcome() {
    // Step 2: Welcome Banner Output
    cout << "Welcome to Stone Paper Scissors!\n";
}

// Task 2 - Define valid moves and target score
// Step 1: Declare Move Collection
const vector<string> MOVES = {"Stone", "Paper", "Scissors"};

// Step 2: Declare Target Score Threshold
const int TARGET_SCORE = 3;

// Task 3 - Create the RoundResult model
struct RoundResult {
    // Step 1: Initialize Winner Identifier
    string winner;

    // Step 2: Initialize Outcome Reason
    string reason;
};

// Task 4 - Implement determineWinner(playerMove, systemMove)
RoundResult determineWinner(const string& playerMove, const string& systemMove) {
    // Step 1: Check Draw Condition
    if (playerMove == systemMove) {
        return {"draw", "Both chose " + playerMove};
    }
    // Step 2: Check Player Victory Conditions
    else if (playerMove == "Stone" && systemMove == "Scissors") {
        return {"player", "Stone crushes Scissors"};
    } else if (playerMove == "Scissors" && systemMove == "Paper") {
        return {"player", "Scissors cuts Paper"};
    } else if (playerMove == "Paper" && systemMove == "Stone") {
        return {"player", "Paper covers Stone"};
    }
    // Step 3: Check System Victory Conditions
    else if (systemMove == "Stone" && playerMove == "Scissors") {
        return {"system", "Stone crushes Scissors"};
    } else if (systemMove == "Scissors" && playerMove == "Paper") {
        return {"system", "Scissors cuts Paper"};
    } else {
        return {"system", "Paper covers Stone"};
    }
}

// Task 5 - Create the Player class constructor
class Player {
public:
    string name;
    int score;

    explicit Player(const string& rawName) {
        // Step 1: Sanitize Player Name
        string trimmed = rawName;
        trimmed.erase(0, trimmed.find_first_not_of(" \t\r\n"));
        if (!trimmed.empty()) {
            trimmed.erase(trimmed.find_last_not_of(" \t\r\n") + 1);
        }
        name = trimmed.empty() ? "Player" : trimmed;

        // Step 2: Initialize Starting Score
        score = 0;
    }

    virtual ~Player() = default;

    // Task 6 - Implement score reset on Player
    void resetScore() {
        // Step 1: Zero Out Score
        score = 0;
    }

    // Task 7 - Implement validated human move input
    virtual string chooseMove() {
        // Step 1: Interactive Prompt Loop
        while (true) {
            // Step 2: Display Choice Menu
            cout << "\n" << name << ", choose your move:\n";
            cout << "  [1] Stone\n";
            cout << "  [2] Paper\n";
            cout << "  [3] Scissors\n";
            cout << "Enter choice (1-3): ";

            // Step 3: Read and Normalize Input
            string input;
            if (!getline(cin, input)) return "Stone";

            string normalized = input;
            transform(normalized.begin(), normalized.end(), normalized.begin(), ::tolower);
            normalized.erase(0, normalized.find_first_not_of(" \t\r\n"));
            if (!normalized.empty()) {
                normalized.erase(normalized.find_last_not_of(" \t\r\n") + 1);
            }

            // Step 4: Validate and Map Choices
            if (normalized == "1" || normalized == "stone") return "Stone";
            if (normalized == "2" || normalized == "paper") return "Paper";
            if (normalized == "3" || normalized == "scissors") return "Scissors";

            // Step 5: Handle Invalid Input
            cout << "Invalid input. Please enter 1, 2, or 3.\n";
        }
    }
};

// Task 8 - Create the SystemPlayer class skeleton
class SystemPlayer : public Player {
public:
    SystemPlayer() : Player("System") {
        // Step 1: Subclass Player Entity
    }

    // Task 9 - Implement system random move choice
    string chooseMove() override {
        // Step 1: Generate Random Move Selection
        int pick = rand() % 3;

        // Step 2: Return Selected Move
        return MOVES[pick];
    }
};

// Task 10 - Create the Game class constructor
class Game {
public:
    Player player;
    SystemPlayer system;
    int targetScore;

    explicit Game(const string& playerName)
        : player(playerName), system(), targetScore(TARGET_SCORE) {
        // Step 1: Instantiate Human Player
        // Step 2: Instantiate System Opponent
        // Step 3: Initialize Target Score Threshold
    }

    // Task 11 - Display the formatted scoreboard
    void displayScore() const {
        // Step 1: Print Scoreboard Top Border
        cout << "\n======================================\n";

        // Step 2: Format Scoreboard Content
        string scoreText = "SCORE: " + player.name + " [ " + to_string(player.score)
                         + " ] - System [ " + to_string(system.score) + " ]";
        int pad = 36 - static_cast<int>(scoreText.size());
        int left = max(pad / 2, 0);
        int right = max(pad - left, 0);
        cout << "|" << string(left, ' ') << scoreText << string(right, ' ') << "|\n";

        // Step 3: Print Scoreboard Bottom Border
        cout << "======================================\n";
    }

    // Task 12 - Play a single round and reveal choices
    void playRound(int roundNum) {
        // Step 1: Print Round Header
        cout << "\n--- Round " << roundNum << " ---\n";

        // Step 2: Collect Opponent Moves
        string playerMove = player.chooseMove();
        string systemMove = system.chooseMove();

        // Step 3: Reveal Choices
        cout << "\n" << player.name << " chose: " << playerMove << "\n";
        cout << "System chose: " << systemMove << "\n";

        // Step 4: Evaluate Outcome
        RoundResult result = determineWinner(playerMove, systemMove);

        // Step 5: Update Scores and Announce Result
        if (result.winner == "draw") {
            cout << "Result: It's a draw! (" << result.reason << ")\n";
        } else if (result.winner == "player") {
            player.score++;
            cout << "Result: " << result.reason << "! " << player.name << " wins Round " << roundNum << "!\n";
        } else {
            system.score++;
            cout << "Result: " << result.reason << "! System wins Round " << roundNum << "!\n";
        }

        // Step 6: Refresh Scoreboard
        displayScore();
    }

    // Task 13 - Implement match champion announcement
    void announceChampion() const {
        // Step 1: Print Match Finished Banner
        cout << "\n===== MATCH FINISHED =====\n";

        // Step 2: Evaluate Final Scores and Crown Champion
        if (player.score > system.score) {
            cout << "MATCH CHAMPION: " << player.name << " wins the match!\n";
        } else {
            cout << "MATCH CHAMPION: System wins the match! Better luck next time!\n";
        }
    }

    // Task 14 - Write the playMatch() loop
    void playMatch() {
        // Step 1: Reset Opponent Scores
        player.resetScore();
        system.resetScore();
        int roundNum = 1;

        // Step 2: Print Match Start Banner
        cout << "\n===== NEW MATCH STARTED =====\n";
        cout << "First to reach " << targetScore << " points wins the match!\n";

        // Step 3: Run Turn-Based Round Loop
        while (player.score < targetScore && system.score < targetScore) {
            playRound(roundNum);
            roundNum++;
        }

        // Step 4: Announce Match Champion
        announceChampion();
    }

    // Task 15 - Implement askReplay()
    static bool askReplay() {
        // Step 1: Interactive Replay Prompt Loop
        while (true) {
            // Step 2: Read and Normalize Confirmation Input
            cout << "\nPlay again? (y/n): ";
            string answer;
            if (!getline(cin, answer)) return false;

            // Step 3: Evaluate Replay Choice
            if (answer == "y" || answer == "Y") return true;
            if (answer == "n" || answer == "N") return false;

            cout << "Please type y or n.\n";
        }
    }

    // Task 16 - Implement playMany() for continuous play
    void playMany() {
        // Step 1: Continuous Match Session Loop
        while (true) {
            // Step 2: Execute Match Lifecycle
            playMatch();

            // Step 3: Prompt for Rematch Confirmation
            if (!askReplay()) {
                // Step 4: Display Session Farewell on Exit
                cout << "\nThanks for playing Stone Paper Scissors!\n";
                break;
            }
        }
    }
};

// Task 17 - Assemble the main() entry point
int main() {
    // Step 1: Initialize System Environment and Welcome Banner
    srand(static_cast<unsigned int>(time(nullptr)));
    printWelcome();

    // Step 2: Capture Player Identity
    cout << "Enter your name: ";
    string playerName;
    getline(cin, playerName);

    // Step 3: Instantiate Game Manager
    Game game(playerName);

    // Step 4: Launch Continuous Match Session
    game.playMany();

    return 0;
}
