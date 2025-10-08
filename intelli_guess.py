import random

#2. Configuration of Dictionary for difficulty levels
# Structure: Key -> (Name, Min_Number, Max_Number)

difficulty_levels = {
    '1': ('Easy', 1, 10),
    '2': ('Medium', 1, 100),
    '3': ('Hard', 1, 1000)
}

def select_difficulty():
    print("\n----- Select Difficulty -----")
    for key, (name, min_val, max_val) in difficulty_levels.items():
        print(f"{key}. {name}: Guess between {min_val} and {max_val}")
        #the f is to combine the string with the variables

        print("-------------------------") 
    

        while True:
            choice = input("Enter your level (1, 2, or 3):").strip()
            if choice in difficulty_levels:
                return difficulty_levels[choice]
            else: 
                print("Invalid selection. Please choose 1, 2, or 3.")
    

def get_valid_guess(min_val, max_val):
    while True:
        # The input prompt uses a dynamic range based on difficulty level
        user_input = input(f"Enter your guess ({min_val}-{max_val}): ")

        #Check for exit condition
        if user_input.lower() == 'exit':
            return 'exit'
        
        #Input Validation and Type Conversion
        try: 
            user_input = int(user_input)
            if min_val <= user_input <= max_val:
                return user_input
            else:
                print(f"Input out of range. Please enter a number between {min_val} and {max_val}.")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def guess_game():
    guess_count = 0

    #STATIC WELCOME MESSAGE
    print("\n=============================================")
    print("          WELCOME TO INTELLI GUESS!           ")
    print("\n=============================================")

    #1. User selects difficulty level
    # Directly unpacking the tuple returned by select_difficulty
    difficulty_level, MIN_NUMBER, MAX_NUMBER = select_difficulty()

    # ---  CONFIRMATION MESSAGE
    print(f"\n--- {difficulty_level} Mode Selected: Guess between {MIN_NUMBER} and {MAX_NUMBER} ---\n")

    #2. Initialize Game State using the chosen constants
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)

     # --- ENHANCED INTRODUCTION (Dynamic Rules) ---
    print(f"\nI have selected a secret number. Start guessing now!")
    print("Your mission is to guess the number in the fewest attempts possible.")
    print("I will give you hints: 'Too High' or 'Too Low'.")
    print("Type 'exit' at any time to quit the game.")
    print("------------------------------------------\n")

    #Main Game Loop
    while True:
        # 3. Pass the dynamic range to the input function
        user_guess = get_valid_guess(MIN_NUMBER, MAX_NUMBER)

        # Handle exit from the helper function
        if user_guess == 'exit':
            print("Thanks for playing! Goodbye!")
            return
        
        guess_count += 1

         # Hint and Win Logic
        if user_guess < secret_number:
            print("Too low! Try a higher number.")
            
        elif user_guess > secret_number:
            print("Too high! Try a lower number.")
            
        else:
            # Win condition
            print("\n🎉 CONGRATULATIONS! 🎉")
            print(f"You guessed the number {secret_number} in {guess_count} attempts!")
            return

def play_again():
    """Asks the user if they want to play another round."""
    while True:
        # Use .strip() to handle accidental spaces
        choice = input("\nPlay again? (y/n): ").lower().strip()
        if choice in ('y', 'yes'):
            return True
        elif choice in ('n', 'no'):
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

if __name__ == '__main__':
    # Top-level loop to manage multiple game sessions
    while True:
        guess_game()
        if not play_again():
            print("Thank you for playing Intelli Guess! Goodbye!")
            break