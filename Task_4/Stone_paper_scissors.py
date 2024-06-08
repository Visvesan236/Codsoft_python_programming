import random

def get_player_choice():
    """Prompts the player for a choice and validates the input."""
    while True:
        player_input = input("Your choice (stone/paper/scissors): ").lower()
        if player_input in valid_choices or player_input == 'exit':
            return player_input
        else:
            print("Invalid choice! Please enter stone, paper, or scissors.")

def get_bot_choice():
    """Randomly selects the bot's choice."""
    return random.choice(valid_choices)

def decide_winner(player, bot):
    """Decides the winner based on player and bot choices."""
    if player == bot:
        return "It's a tie!"
    elif (player == "stone" and bot == "scissors") or \
         (player == "paper" and bot == "stone") or \
         (player == "scissors" and bot == "paper"):
        return "You win!"
    else:
        return "You lose!"

def start_game():
    """Main game loop for playing Stone, Paper, Scissors."""
    print("Welcome to Stone, Paper, Scissors!")
    print("Type 'exit' to end the game.")

    while True:
        player_choice = get_player_choice()
        if player_choice == 'exit':
            break

        bot_choice = get_bot_choice()
        print(f"Bot's choice: {bot_choice}")

        outcome = decide_winner(player_choice, bot_choice)
        print(outcome)

    print("Thank you for playing!")
valid_choices = ["stone", "paper", "scissors"]
start_game()
