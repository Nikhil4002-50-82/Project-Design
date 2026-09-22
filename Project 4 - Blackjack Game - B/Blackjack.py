# Task 1 - Create the entry file and print welcome message
# Step 1: Entry File Setup
import random


def print_welcome():
    # Step 2: Welcome Banner Output
    print("Welcome to Blackjack!")


# Task 2 - Define standard ranks and suits constants
# Step 1: Declare Rank Collection
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

# Step 2: Declare Suit Collection
SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]


# Task 3 - Create the Card class
class Card:
    def __init__(self, rank, suit):
        # Step 1: Initialize Card Rank and Suit
        self.rank = rank
        self.suit = suit

    def __str__(self):
        # Step 2: Format Card Description
        return f"{self.rank} of {self.suit}"


# Task 4 - Create and populate the 52-card deck
def create_deck():
    # Step 1: Initialize Empty Deck Collection
    deck = []

    # Step 2: Populate Combinations with Nested Loops
    for suit in SUITS:
        for rank in RANKS:
            deck.append(Card(rank, suit))

    # Step 3: Return Completed Deck
    return deck


# Task 5 - Shuffle the deck
def shuffle_deck(deck):
    # Step 1: Receive Deck Reference
    # Step 2: Randomize Card Positions in Place
    random.shuffle(deck)


# Task 6 - Deal a card from the deck
def deal_card(deck):
    # Step 1: Extract Top Card from Collection
    # Step 2: Return Dealt Card
    return deck.pop()


# Task 7 - Calculate hand value with automatic Ace adjustment
def calculate_score(hand):
    # Step 1: Initialize Point Accumulator and Ace Counter
    total = 0
    ace_count = 0

    # Step 2: Accumulate Card Values and Count Aces
    for card in hand:
        if card.rank in ["Jack", "Queen", "King"]:
            total += 10
        elif card.rank == "Ace":
            total += 11
            ace_count += 1
        else:
            total += int(card.rank)

    # Step 3: Dynamically Downgrade Aces to Avoid Busting
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1

    # Step 4: Return Calculated Hand Score
    return total


# Task 8 - Display hands with hidden hole card support
def display_hand(owner_name, hand, hide_first_card=False):
    # Step 1: Check Hole Card Masking Flag
    if hide_first_card:
        # Step 2: Render Masked Hand for Dealer
        print(f"{owner_name}'s Hand: [Hidden Card], {hand[1]}")
    else:
        # Step 3: Render Formatted Visible Hand with Score
        cards_str = ", ".join(str(card) for card in hand)
        score = calculate_score(hand)
        print(f"{owner_name}'s Hand ({score}): {cards_str}")


# Task 9 - Prompt and validate Player choice (Hit or Stand)
def get_player_choice():
    # Step 1: Interactive Input Prompt Loop
    while True:
        # Step 2: Clean and Normalize Input
        choice = input("\nWould you like to (H)it or (S)tand? ").strip().lower()

        # Step 3: Evaluate Valid Choice or Re-prompt
        if choice in ["h", "hit"]:
            return "h"
        elif choice in ["s", "stand"]:
            return "s"
        else:
            print("Invalid input. Please enter 'h' to hit or 's' to stand.")


# Task 10 - Execute Dealer's automated turn
def play_dealer_turn(deck, dealer_hand):
    # Step 1: Announce Dealer Turn and Reveal Hole Card
    print("\n--- Dealer's Turn ---")
    display_hand("Dealer", dealer_hand, hide_first_card=False)

    # Step 2: Automated Hit Loop While Score Under 17
    while calculate_score(dealer_hand) < 17:
        # Step 3: Draw Card, Announce Draw, and Refresh Display
        card = deal_card(deck)
        dealer_hand.append(card)
        print(f"Dealer hits and draws: {card}")
        display_hand("Dealer", dealer_hand, hide_first_card=False)

    # Step 4: Evaluate and Announce Dealer Stand or Bust
    score = calculate_score(dealer_hand)
    if score > 21:
        print("Dealer busted!")
    else:
        print(f"Dealer stands with {score}.")


# Task 11 - Determine and announce round outcome
def determine_outcome(player_hand, dealer_hand):
    # Step 1: Calculate Final Scores and Display Matchup Summary
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print("\n===== ROUND RESULT =====")
    display_hand("Player", player_hand)
    display_hand("Dealer", dealer_hand)

    # Step 2: Check Player Bust Condition
    if player_score > 21:
        print("\nDealer wins! You went over 21.")
        return "dealer"

    # Step 3: Check Dealer Bust Condition
    elif dealer_score > 21:
        print("\nYou win! Dealer went over 21.")
        return "player"

    # Step 4: Compare Final Hand Scores and Announce Result
    elif player_score > dealer_score:
        print(f"\nYou win! Your {player_score} beats Dealer's {dealer_score}.")
        return "player"
    elif dealer_score > player_score:
        print(f"\nDealer wins! Dealer's {dealer_score} beats your {player_score}.")
        return "dealer"
    else:
        # Step 5: Return Standard Outcome Identifier
        print(f"\nIt's a push (tie)! Both have {player_score}.")
        return "tie"


# Task 12 - Manage and display session scoreboard
def display_scoreboard(player_wins, dealer_wins, ties):
    # Step 1: Format Scoreboard Card Border
    print("\n------------------------------------")
    # Step 2: Print Cumulative Tally Line
    print(f"SCOREBOARD: Player: {player_wins} | Dealer: {dealer_wins} | Ties: {ties}")
    print("------------------------------------")


# Task 13 - Create BlackjackGame class and implement playRound()
class BlackjackGame:
    def __init__(self):
        # Step 1: Initialize Session Score Counters
        self.player_wins = 0
        self.dealer_wins = 0
        self.ties = 0

    def update_scores(self, outcome):
        # Helper for updating scores
        if outcome == "player":
            self.player_wins += 1
        elif outcome == "dealer":
            self.dealer_wins += 1
        elif outcome == "tie":
            self.ties += 1
        display_scoreboard(self.player_wins, self.dealer_wins, self.ties)

    def play_round(self):
        # Step 2: Generate, Shuffle, and Deal Opening Cards
        deck = create_deck()
        shuffle_deck(deck)

        player_hand = [deal_card(deck), deal_card(deck)]
        dealer_hand = [deal_card(deck), deal_card(deck)]

        # Step 3: Render Opening Hands with Dealer Hole Card Masked
        print("\n===== NEW BLACKJACK ROUND =====")
        display_hand("Dealer", dealer_hand, hide_first_card=True)
        display_hand("Player", player_hand, hide_first_card=False)

        # Step 4: Check Natural Opening Blackjack
        if calculate_score(player_hand) == 21:
            print("\nBlackjack! You have 21!")
            outcome = determine_outcome(player_hand, dealer_hand)
            self.update_scores(outcome)
            return

        # Step 5: Execute Interactive Player Turn Loop
        while calculate_score(player_hand) < 21:
            choice = get_player_choice()
            if choice == "h":
                card = deal_card(deck)
                player_hand.append(card)
                print(f"\nYou drew: {card}")
                display_hand("Player", player_hand, hide_first_card=False)
            else:
                print("\nYou chose to stand.")
                break

        if calculate_score(player_hand) > 21:
            print(f"\nYou busted with {calculate_score(player_hand)}!")
            outcome = determine_outcome(player_hand, dealer_hand)
            self.update_scores(outcome)
            return

        # Step 6: Execute Dealer Turn and Resolve Outcome
        play_dealer_turn(deck, dealer_hand)
        outcome = determine_outcome(player_hand, dealer_hand)
        self.update_scores(outcome)

    # Task 14 - Implement askReplay()
    @staticmethod
    def ask_replay():
        # Step 1: Interactive Rematch Confirmation Loop
        while True:
            # Step 2: Normalize Input and Return Decision
            choice = input("\nPlay another round? (y/n): ").strip().lower()
            if choice in ["y", "yes"]:
                return True
            elif choice in ["n", "no"]:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")

    # Task 15 - Implement playMany() for continuous play
    def play_many(self):
        # Step 1: Display Welcome Greeting
        print_welcome()

        # Step 2: Continuous Round Execution Loop
        while True:
            self.play_round()

            # Step 3: Prompt Replay and Present Final Session Stats on Exit
            if not self.ask_replay():
                print("\nFinal Session Stats:")
                display_scoreboard(self.player_wins, self.dealer_wins, self.ties)
                print("Thanks for playing Blackjack!")
                break


# Task 16 - Assemble the main() entry point
def main():
    # Step 1: Instantiate Game Manager
    game = BlackjackGame()

    # Step 2: Launch Continuous Session
    game.play_many()


if __name__ == "__main__":
    main()
