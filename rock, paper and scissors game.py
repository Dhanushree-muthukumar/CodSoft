import random
def play_game():
    choice = ["rock", "paper", "scissors"]
    user_score, computer_score = 0, 0

    while True:
        user_choice = input("\nChoose rock, paper, or scissors (or type 'quit' to exit: ").lower()
        if user_choice == "quit":
            print(f"\nFiinal Score - You: {user_score}, computer: {computer_score}\nThanks for playing!")
            break
        if user_choice not in choice:
            print("Invalid choice. Try again.")
            continue
        computer_choice = random.choice(choice)
        print(f"You chose: {user_choice}, Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win")
            user_score += 1
        else:
            print("You lose")
            computer_score += 1

        print(f"Score - you: {user_score}, computer: {computer_score}")

play_game()
