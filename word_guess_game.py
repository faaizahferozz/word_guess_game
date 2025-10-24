import random
import json
import os

# List of words for guessing
WORDS = ["python", "developer", "terminal", "hangman", "portfolio", "algorithm", "data"]
HIGHSCORE_FILE = "highscore.json"

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

# Choose a random word
def choose_word():
    return random.choice(WORDS)

# Display current word state
def display_state(word, guessed):
    return " ".join([c if c in guessed else "_" for c in word])

# Main game loop
def play():
    word = choose_word()
    guessed = set()
    attempts_left = 7

    while attempts_left > 0 and set(word) - guessed:
        print("\nWord:", display_state(word, guessed))
        print("Guessed letters:", " ".join(sorted(guessed)) or "-")
        print("Attempts left:", attempts_left)
        guess = input("Guess a letter: ").strip().lower()

        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Enter a single valid letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts_left -= 1

    if set(word) - guessed == set():
        print(f"\nYou won! The word was: {word}")
        return True, len(guessed)
    else:
        print(f"\nYou lost! The word was: {word}")
        return False, len(guessed)

# Run the game
def main():
    high = load_highscore()
    print("Highscore (fewest guesses):", high.get("name"), high.get("guesses"))
    win, guesses = play()
    if win and guesses < high.get("guesses", 999):
        name = input("New highscore! Enter your name: ").strip()
        save_highscore({"name": name, "guesses": guesses})
        print("Highscore saved!")

if __name__ == "__main__":
    main()