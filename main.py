import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        return "player"
    else:
        return "computer"

def play_game:
    print("========================================")
    print("   WELCOME TO ROCK, PAPER, SCISSORS!    ")
    print("========================================")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.\n")

    player_score = 0
    computer_score = 0
    ties = 0

    while True:
        player_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower().strip()

        if player_choice == 'quit':
            print("\nThanks for playing!")
            break

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please choose rock, paper, or scissors.\n")
            continue

        computer_choice = get_computer_choice()
        print(f"\nYou chose: {player_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")

        result = determine_winner(player_choice, computer_choice)

        if result == "tie":
            print("It's a tie!\n")
            ties += 1
        elif result == "player":
            print("🎉 You win this round!\n")
            player_score += 1
        else:
            print("💻 Computer wins this round!\n")
            computer_score += 1

        print("-" * 40)
        print(f"SCOREBOARD -> You: {player_score} | Computer: {computer_score} | Ties: {ties}")
        print("-" * 40 + "\n")

if __name__ == "__main__":
    play_game()