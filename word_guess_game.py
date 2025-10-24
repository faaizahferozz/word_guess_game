import random
import json
import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Highscore file
HIGHSCORE_FILE = "highscore.json"

# ASCII Hangman stages
HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

# Kashmiri words with hints
WORDS_WITH_HINTS = {
    "haakh": "Favourite leafy vegetable",
    "yemberzal": "Pampore is famous for?",
    "phiran": "Keeps us warm in winter",
    "noonchai": "Pink tea",
    "wanwun": "Weddings are incomplete without?",
    "wazwan": "Grand feast",
    "kulche": "noon chai te?",
    "roganjosh": "A part of wazwan",
    "tabakmaaz": "Everyone's favourite wazwan dish",
    "golaab": "Fragrant flower",
    "rouf": "Favourite dance",
    "chinar": "Older than the occupation",
    "sheermal": "Sweet bread",
    "kangir": "If you drop it, you're dead",
    "pashmina": "tere goat ka wo fur. iykyk",
    "rajbagh": "Favourite gedi spot",
    "rantas": "All my enemies",
    "harud": "Favourite season",
}

# Load highscore
def load_highscore():
    if not os.path.exists(HIGHSCORE_FILE):
        return {"name": "", "guesses": 999}
    with open(HIGHSCORE_FILE, "r") as f:
        return json.load(f)

# Save highscore
def save_highscore(data):
    with open(HIGHSCORE_FILE, "w") as f:
        json.dump(data, f)

# Choose a random word and its hint
def choose_word():
    word, hint = random.choice(list(WORDS_WITH_HINTS.items()))
    return word, hint

# Display current word state
def display_state(word, guessed):
    return " ".join([c if c in guessed else "_" for c in word])

# Main game loop
def play():
    word, hint = choose_word()
    guessed = set()
    attempts_left = 6
    hint_used = False

    while attempts_left >= 0 and set(word) - guessed:
        print(Fore.CYAN + HANGMAN_PICS[6 - attempts_left])
        print(Fore.YELLOW + "Word: " + display_state(word, guessed))
        print(Fore.MAGENTA + "Guessed letters: " + " ".join(sorted(guessed)) if guessed else "-")
        print(Fore.GREEN + f"Attempts left: {attempts_left}")

        # Offer optional hint
        if not hint_used:
            use_hint = input(Fore.WHITE + "Do you want a hint? (y/n): ").strip().lower()
            if use_hint == "y":
                print(Fore.BLUE + f"Hint: {hint}")
                hint_used = True

        guess = input(Fore.WHITE + "Guess a letter: ").strip().lower()

        if not guess or len(guess) != 1 or not guess.isalpha():
            print(Fore.RED + "Enter a single valid letter.")
            continue

        if guess in guessed:
            print(Fore.RED + "You already guessed that letter.")
            continue

        guessed.add(guess)

        if guess in word:
            print(Fore.GREEN + "Good guess!")
        else:
            print(Fore.RED + "Wrong guess!")
            attempts_left -= 1

    if set(word) - guessed == set():
        print(Fore.GREEN + f"\nYou won! The word was: {word}")
        return True, len(guessed)
    else:
        print(Fore.RED + f"\nYou lost! The word was: {word}")
        print(Fore.CYAN + HANGMAN_PICS[6])
        return False, len(guessed)

# Run the game
def main():
    high = load_highscore()
    while True:
        print(Fore.BLUE + f"Highscore (fewest guesses): {high.get('name')} - {high.get('guesses')}")
        win, guesses = play()
        if win and guesses < high.get("guesses", 999):
            name = input(Fore.WHITE + "New highscore! Enter your name: ").strip()
            save_highscore({"name": name, "guesses": guesses})
            print(Fore.GREEN + "Highscore saved!")

        play_again = input(Fore.WHITE + "\nDo you want to play again? (y/n): ").strip().lower()
        if play_again != "y":
            print(Fore.CYAN + "Thanks for playing!")
            break

if __name__ == "__main__":
    main()