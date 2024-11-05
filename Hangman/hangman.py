import random
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# ASCII art stages for each failed attempt
HANGMAN_STAGES = [
    """
     ------
     |    |
     |
     |
     |
     |
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    """
]

def read_file(file_name):
    """Reads words from a file."""
    with open(file_name) as f:
        lines = f.read().splitlines()
    return lines

def select_random_word(words, difficulty):
    """Selects a random word based on the chosen difficulty."""
    if difficulty == 'easy':
        word_list = [word for word in words if 3 <= len(word) <= 4]
    elif difficulty == 'medium':
        word_list = [word for word in words if 5 <= len(word) <= 6]
    else:
        word_list = [word for word in words if len(word) >= 7]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """Displays the current state of the word with guessed letters."""
    displayed_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print("Word:", displayed_word)

def get_user_input():
    """Prompts the user for input and validates it."""
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        elif len(guess) > 1:
            print(Fore.RED + "Invalid input. Please enter only a single letter, not multiple letters.")
        else:
            print(Fore.RED + "Invalid input. Please enter a single letter.")

def choose_difficulty():
    """Prompts the user to choose a difficulty level."""
    difficulty = input("Choose difficulty (easy, medium, hard): ").strip().lower()
    if difficulty == 'easy':
        return 'easy', 8
    elif difficulty == 'medium':
        return 'medium', 6
    elif difficulty == 'hard':
        return 'hard', 4
    else:
        print(Fore.RED + "Invalid choice. Defaulting to medium difficulty.")
        return 'medium', 6

def show_hangman(attempts_left):
    """Displays the hangman based on remaining attempts."""
    stage_index = 6 - attempts_left
    print(Fore.RED + HANGMAN_STAGES[stage_index])

def run_game(file_name):
    """Main function to run the Hangman game."""
    while True:
        words = read_file(file_name)
        difficulty, attempts_left = choose_difficulty()
        word = select_random_word(words, difficulty).lower()
        guessed_letters = set()
        missed_letters = set()
        score = 0
        hints_used = 0
        start_time = time.time()  # Track the start time for the timer
        
        print(Fore.YELLOW + "Welcome to Hangman!")
        print(Fore.YELLOW + f"You have {attempts_left} attempts to guess the word.")
        
        while attempts_left > 0:
            display_word(word, guessed_letters)
            print("Missed letters:", ' '.join(sorted(missed_letters)))
            
            guess_start = time.time()  # Start timer for this guess
            guess = get_user_input()
            guess_time = time.time() - guess_start  # Calculate guess time
            
            if guess == "hint":
                if hints_used == 0:
                    hints_used += 1
                    attempts_left -= 1
                    for letter in word:
                        if letter not in guessed_letters:
                            print(Fore.CYAN + f"Hint: Try the letter '{letter}'!")
                            break
                else:
                    print(Fore.RED + "You've already used your hint.")
            
            elif guess in guessed_letters or guess in missed_letters:
                print(Fore.CYAN + "You already guessed that letter.")
            elif guess in word:
                print(Fore.GREEN + "Good guess!")
                guessed_letters.add(guess)
                score += 10  # Points for correct guess
                
                if guess_time < 5:  # Bonus points for fast guessing
                    score += 2
                    print(Fore.GREEN + "Quick guess! Bonus points awarded.")
            else:
                print(Fore.RED + "Wrong guess.")
                attempts_left -= 1
                missed_letters.add(guess)
                score -= 5  # Penalty for wrong guess
                print(Fore.RED + f"Attempts left: {attempts_left}")
                show_hangman(attempts_left)
            
            if all(letter in guessed_letters for letter in word):
                total_time = int(time.time() - start_time)
                print(Fore.GREEN + f"Congratulations! You've guessed the word '{word}'.")
                print(Fore.YELLOW + f"Total time: {total_time} seconds")
                
                # Bonus for unused attempts
                score += attempts_left * 5
                print(Fore.GREEN + f"Score: {score} (including {attempts_left * 5} bonus points for remaining attempts)")
                break
        else:
            print(Fore.RED + f"Game Over! The word was '{word}'. Your score: {score}")

        # Ask to restart
        restart = input("Do you want to play again? (yes/no): ").strip().lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    run_game('short_words.txt')
