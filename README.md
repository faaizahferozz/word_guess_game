<img width="263" height="455" alt="Screenshot 2025-10-24 at 8 07 56 PM" src="https://github.com/user-attachments/assets/3d97ca18-83a6-4b2c-ad16-22e3ef33e437" />Kashmiri Word Guessing Game 
A fun and interactive Word Guessing Game inspired by Hangman, featuring Kashmiri words, optional hints and ASCII hangman.  

Features
- Kashmiri words: Learn and guess traditional Kashmiri words.  
- Optional hints: Get a hint if you’re stuck.  
- ASCII hangman: Classic visual representation of the hangman.  
- Colorful terminal output using `colorama`.  
- Highscore tracking: Save the player with the fewest guesses. 

Words Included -

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
    "harud": "Favourite season".

Setup Instructions

1. Clone the repository -
  "```bash " (remove double quotes)
  git clone https://github.com/faaizahferozz/word_guess_game.git
  cd word_guess_game
2. Create a virtual environment -
  python3 -m venv venv
  source venv/bin/activate
3. Install dependencies -
  pip install colorama
4. Run the game -
  python word_guess_game.py



How to Play

	1.	The game chooses a random Kashmiri word.
	2.	You have 6 attempts to guess the word one letter at a time.
	3.	Optionally, you can ask for a hint.
	4.	Each wrong guess draws the ASCII hangman.
	5.	Win by guessing all letters before the hangman is complete.
	6.	Highscores are saved in highscore.json.

Game Play Example 

Word: _ _ _ _ _ _ _ _ _
Guessed letters: -
Attempts left: 6
Do you want a hint? (y/n): y
Hint: Famous Kashmiri meat curry
Guess a letter: r
Good guess!
    
![Uploa<img width="263" height="455" alt="Screenshot 2025-10-24 at 8 08 09 PM" src="https://github.com/user-attachments/assets/a6587625-82ee-48e2-8ab6-b55278f6adf6" />
ding Screenshot 2025-10-24 at 8.07.56 PM.png…]()

    

