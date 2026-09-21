import random

# Task 1 - Create the entry file and print welcome message
# Step 1: Entry File Setup
# Step 2: Welcome Banner Output
def print_welcome():
    print("Welcome to Bingo!")


# Task 2 - Define the 12 winning lines and FREE center index
# Step 1: Center Index Constant
FREE_INDEX = 12

# Step 2: Winning Lines Matrix
WIN_LINES = [
    (0, 1, 2, 3, 4), (5, 6, 7, 8, 9), (10, 11, 12, 13, 14),        # rows
    (15, 16, 17, 18, 19), (20, 21, 22, 23, 24),
    (0, 5, 10, 15, 20), (1, 6, 11, 16, 21), (2, 7, 12, 17, 22),    # columns
    (3, 8, 13, 18, 23), (4, 9, 14, 19, 24),
    (0, 6, 12, 18, 24), (4, 8, 12, 16, 20),                        # diagonals
]


# Task 3 - Create the Card class and generate numbers
class Card:
    def __init__(self):
        # Step 1: State Initialization
        self.numbers = self.generate()
        self.marked = [False] * 25
        self.marked[FREE_INDEX] = True

    def generate(self):
        cells = [None] * 25
        low = [1, 16, 31, 46, 61]
        high = [15, 30, 45, 60, 75]

        # Step 2: Column-Wise Number Generation
        for col in range(5):
            col_numbers = random.sample(range(low[col], high[col] + 1), 5)
            # Step 3: 1D Grid Coordinate Mapping & Center FREE Placement
            for row in range(5):
                cells[row * 5 + col] = col_numbers[row]
        cells[FREE_INDEX] = "FREE"
        return cells

    # Task 4 - Display the card
    def display(self, title="Your Card"):
        # Step 1: Header Title & Row Iteration
        print(f"\n{title}")
        for row in range(5):
            cells_in_row = []
            # Step 2: Cell Formatting & Daub Indicator
            for col in range(5):
                idx = row * 5 + col
                value = self.numbers[idx]
                text = str(value)
                if self.marked[idx]:
                    text = f"*{text}*"
                cells_in_row.append(text.center(6))
            # Step 3: Pipe Separators & Horizontal Dividers
            print("|".join(cells_in_row))
            if row != 4:
                print("-" * 34)

    # Task 5 - Implement mark(number)
    def mark(self, number):
        # Step 1: Linear Search for Target Value
        for i in range(25):
            # Step 2: Daub & Confirmation Return
            if self.numbers[i] == number and not self.marked[i]:
                self.marked[i] = True
                return True
        return False

    # Task 6 - Implement checkWin()
    def check_win(self):
        # Step 1: Iterate Winning Line Definitions
        for line in WIN_LINES:
            # Step 2: Line Verification & Early Exit
            line_complete = True
            for idx in line:
                if not self.marked[idx]:
                    line_complete = False
                    break
            if line_complete:
                return True
        return False


# Task 7 - Create the Player class
class Player:
    def __init__(self, raw_name):
        # Step 1: Name Sanitization & Default Assignment
        if raw_name and raw_name.strip():
            self.name = raw_name.strip()
        else:
            self.name = "Player"
        # Step 2: Card Ownership & Victory Flag
        self.card = Card()
        self.has_won = False


# Task 8 - Build a list of players
def build_players():
    # Step 1: Player Count Prompt & Defensive Validation
    while True:
        user_input = input("How many players (1-6)? ").strip()
        if user_input.isdigit() and 1 <= int(user_input) <= 6:
            num_players = int(user_input)
            break
        print("Please enter a number from 1 to 6.")

    # Step 2: Roster Instantiation Loop
    players = []
    for i in range(1, num_players + 1):
        name = input(f"Enter name for Player {i}: ")
        players.append(Player(name))
    return players


# Task 9 - Create the Game class skeleton
class Game:
    def __init__(self, players):
        # Step 1: State Binding
        self.players = players
        self.number_pool = []
        self.called_numbers = []
        # Step 2: Number Pool Generation & Shuffling
        self.reset_number_pool()

    def reset_number_pool(self):
        self.number_pool = list(range(1, 76))
        random.shuffle(self.number_pool)
        self.called_numbers = []

    # Task 10 - Implement drawNumber()
    def draw_number(self):
        # Step 1: Draw from Pool
        number = self.number_pool.pop()
        # Step 2: History Logging & Return
        self.called_numbers.append(number)
        return number

    # Task 11 - Broadcast a drawn number to every player
    def broadcast(self, number):
        # Step 1: Roster Broadcast Loop
        for player in self.players:
            # Step 2: Console Daub Notification
            if player.card.mark(number):
                print(f"  -> marked on {player.name}'s card")

    # Task 12 - Check every player for a win, every round
    def check_winners(self):
        # Step 1: Winner Collection Scan
        winners = []
        for player in self.players:
            # Step 2: Flag State & Winner Accumulation
            if player.card.check_win():
                player.has_won = True
                winners.append(player)
        return winners

    # Task 13 - Write the interactive play() loop
    def play(self):
        # Step 1: Match Setup & Card Reveal
        self.reset_number_pool()
        for player in self.players:
            player.has_won = False
            player.card = Card()
            input(f"\n{player.name}, press Enter to draw your card:")
            player.card.display(f"{player.name}'s Card")

        # Step 2: Match Start Indicator & Status Tracking
        print("\n===== MATCH STARTED =====")
        winners = []
        turn = 0

        # Step 3: Turn-Based Draw Loop & Interactive Pacing
        while self.number_pool and not winners:
            active_player = self.players[turn % len(self.players)]
            input(f"\n{active_player.name}, press Enter to draw the next number:")
            number = self.draw_number()
            print(f"\nNumber called: {number}  (draw #{len(self.called_numbers)})")

            # Step 4: Broadcast, Win Check & Turn Increment
            self.broadcast(number)
            winners = self.check_winners()
            turn += 1

        # Step 5: Match Conclusion Dispatch
        self.announce_result(winners)

    # Task 14 - Announce the result
    def announce_result(self, winners):
        # Step 1: Branch on Win vs. Draw
        if winners:
            # Step 2: Winner Showcase & Final Card Grid Display
            for player in self.players:
                player.card.display(f"{player.name}'s Final Card")
            names = ", ".join(player.name for player in winners)
            print(f"\nBINGO! {names} won after {len(self.called_numbers)} numbers called!")
        else:
            # Step 3: Exhausted Pool Draw Message
            print("\nAll 75 numbers were called with no winner. It's a draw!")

    # Task 15 - Implement askReplay()
    @staticmethod
    def ask_replay():
        # Step 1: Interactive Loop & Choice Prompt
        while True:
            answer = input("Play again? (y/n): ").strip().lower()
            # Step 2: Sanitization & Normalized Matching
            if answer == "y":
                return True
            if answer == "n":
                return False
            print("Please type y or n.")

    # Task 16 - Implement playMany()
    def play_many(self):
        # Step 1: Multi-Match Indefinite Loop
        while True:
            self.play()
            # Step 2: Rematch Evaluation & Exit Farewell
            if not self.ask_replay():
                print("Thanks for playing Bingo!")
                break


# Task 17 - Assemble the main() entry point
def main():
    # Step 1: Component Initialization Pipeline
    print_welcome()
    players = build_players()
    game = Game(players)
    # Step 2: Kickoff Application Session
    game.play_many()


if __name__ == "__main__":
    main()