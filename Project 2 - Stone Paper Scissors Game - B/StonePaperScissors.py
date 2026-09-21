# Task 1 - Create the entry file and print welcome message
# Step 1: Entry File Setup
import random


def print_welcome():
    # Step 2: Welcome Banner Output
    print("Welcome to Stone Paper Scissors!")


# Task 2 - Define valid moves and target score
# Step 1: Declare Move Collection
MOVES = ["Stone", "Paper", "Scissors"]

# Step 2: Declare Target Score Threshold
TARGET_SCORE = 3


# Task 3 - Create the RoundResult model
class RoundResult:
    def __init__(self, winner, reason):
        # Step 1: Initialize Winner Identifier
        self.winner = winner

        # Step 2: Initialize Outcome Reason
        self.reason = reason


# Task 4 - Implement determineWinner(playerMove, systemMove)
def determine_winner(player_move, system_move):
    # Step 1: Check Draw Condition
    if player_move == system_move:
        return RoundResult("draw", f"Both chose {player_move}")

    # Step 2: Check Player Victory Conditions
    elif player_move == "Stone" and system_move == "Scissors":
        return RoundResult("player", "Stone crushes Scissors")
    elif player_move == "Scissors" and system_move == "Paper":
        return RoundResult("player", "Scissors cuts Paper")
    elif player_move == "Paper" and system_move == "Stone":
        return RoundResult("player", "Paper covers Stone")

    # Step 3: Check System Victory Conditions
    elif system_move == "Stone" and player_move == "Scissors":
        return RoundResult("system", "Stone crushes Scissors")
    elif system_move == "Scissors" and player_move == "Paper":
        return RoundResult("system", "Scissors cuts Paper")
    else:
        return RoundResult("system", "Paper covers Stone")


# Task 5 - Create the Player class constructor
class Player:
    def __init__(self, name):
        # Step 1: Sanitize Player Name
        self.name = name.strip() if name and name.strip() else "Player"

        # Step 2: Initialize Starting Score
        self.score = 0

    # Task 6 - Implement score reset on Player
    def reset_score(self):
        # Step 1: Zero Out Score
        self.score = 0

    # Task 7 - Implement validated human move input
    def choose_move(self):
        # Step 1: Interactive Prompt Loop
        while True:
            # Step 2: Display Choice Menu
            print(f"\n{self.name}, choose your move:")
            print("  [1] Stone")
            print("  [2] Paper")
            print("  [3] Scissors")

            # Step 3: Read and Normalize Input
            choice = input("Enter choice (1-3): ").strip().lower()

            # Step 4: Validate and Map Choices
            if choice in ["1", "stone"]:
                return "Stone"
            elif choice in ["2", "paper"]:
                return "Paper"
            elif choice in ["3", "scissors"]:
                return "Scissors"

            # Step 5: Handle Invalid Input
            print("Invalid input. Please enter 1, 2, or 3.")


# Task 8 - Create the SystemPlayer class skeleton
class SystemPlayer(Player):
    def __init__(self):
        # Step 1: Subclass Player Entity
        super().__init__("System")

    # Task 9 - Implement system random move choice
    def choose_move(self):
        # Step 1: Generate Random Move Selection
        selected_move = random.choice(MOVES)

        # Step 2: Return Selected Move
        return selected_move


# Task 10 - Create the Game class constructor
class Game:
    def __init__(self, player_name):
        # Step 1: Instantiate Human Player
        self.player = Player(player_name)

        # Step 2: Instantiate System Opponent
        self.system = SystemPlayer()

        # Step 3: Initialize Target Score Threshold
        self.target_score = TARGET_SCORE

    # Task 11 - Display the formatted scoreboard
    def display_score(self):
        # Step 1: Print Scoreboard Top Border
        print("\n======================================")

        # Step 2: Format Scoreboard Content
        score_text = f"SCORE: {self.player.name} [ {self.player.score} ] - System [ {self.system.score} ]"
        print(f"| {score_text.center(34)} |")

        # Step 3: Print Scoreboard Bottom Border
        print("======================================")

    # Task 12 - Play a single round and reveal choices
    def play_round(self, round_num):
        # Step 1: Print Round Header
        print(f"\n--- Round {round_num} ---")

        # Step 2: Collect Opponent Moves
        player_move = self.player.choose_move()
        system_move = self.system.choose_move()

        # Step 3: Reveal Choices
        print(f"\n{self.player.name} chose: {player_move}")
        print(f"System chose: {system_move}")

        # Step 4: Evaluate Outcome
        result = determine_winner(player_move, system_move)

        # Step 5: Update Scores and Announce Result
        if result.winner == "draw":
            print(f"Result: It's a draw! ({result.reason})")
        elif result.winner == "player":
            self.player.score += 1
            print(f"Result: {result.reason}! {self.player.name} wins Round {round_num}!")
        else:
            self.system.score += 1
            print(f"Result: {result.reason}! System wins Round {round_num}!")

        # Step 6: Refresh Scoreboard
        self.display_score()

    # Task 13 - Implement match champion announcement
    def announce_champion(self):
        # Step 1: Print Match Finished Banner
        print("\n===== MATCH FINISHED =====")

        # Step 2: Evaluate Final Scores and Crown Champion
        if self.player.score > self.system.score:
            print(f"MATCH CHAMPION: {self.player.name} wins the match!")
        else:
            print("MATCH CHAMPION: System wins the match! Better luck next time!")

    # Task 14 - Write the playMatch() loop
    def play_match(self):
        # Step 1: Reset Opponent Scores
        self.player.reset_score()
        self.system.reset_score()
        round_num = 1

        # Step 2: Print Match Start Banner
        print("\n===== NEW MATCH STARTED =====")
        print(f"First to reach {self.target_score} points wins the match!")

        # Step 3: Run Turn-Based Round Loop
        while self.player.score < self.target_score and self.system.score < self.target_score:
            self.play_round(round_num)
            round_num += 1

        # Step 4: Announce Match Champion
        self.announce_champion()

    # Task 15 - Implement askReplay()
    @staticmethod
    def ask_replay():
        # Step 1: Interactive Replay Prompt Loop
        while True:
            # Step 2: Read and Normalize Confirmation Input
            answer = input("\nPlay again? (y/n): ").strip().lower()

            # Step 3: Evaluate Replay Choice
            if answer == "y":
                return True
            elif answer == "n":
                return False
            print("Please type y or n.")

    # Task 16 - Implement playMany() for continuous play
    def play_many(self):
        # Step 1: Continuous Match Session Loop
        while True:
            # Step 2: Execute Match Lifecycle
            self.play_match()

            # Step 3: Prompt for Rematch Confirmation
            if not self.ask_replay():
                # Step 4: Display Session Farewell on Exit
                print("\nThanks for playing Stone Paper Scissors!")
                break


# Task 17 - Assemble the main() entry point
def main():
    # Step 1: Initialize System Environment and Welcome Banner
    print_welcome()

    # Step 2: Capture Player Identity
    player_name = input("Enter your name: ")

    # Step 3: Instantiate Game Manager
    game = Game(player_name)

    # Step 4: Launch Continuous Match Session
    game.play_many()


if __name__ == "__main__":
    main()
