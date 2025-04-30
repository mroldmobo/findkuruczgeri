# findkuruczgeri
# 🔍 Name Legends: The Hunt for Kurucz Gergely

_A text-based adventure where you search for the legendary coder (1 in a million chance!)_

![Gameplay Screenshot](screenshot.png) *(Example screenshot placeholder)*

## 🎮 Features
- **1 in 1,000,000 chance** to find the mythical coder
- Energy management system (search vs rest)
- Simple ASCII art for special events
- Multiple character types to discover
- Win/lose conditions with different endings

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/name-legends.git

    Install dependencies (just Colorama for colors):
    bash

    pip install colorama

🕹️ How to Play
Command	Action
search / s	Spend 10 energy to search
rest / r	Recover 20-40 energy
status	Show current stats
save	Save your progress
load	Load saved game
quit / q	Exit the game

Win Condition: Find Kurucz Gergely or earn 1000 fame
Lose Condition: Run out of energy
📂 File Structure

.
├── game.py            # Main game script
├── README.md          # This file
├── requirements.txt   # Dependencies
└── savefile.json      # Auto-generated save file

🛠️ Customization

Edit these values in game.py:
python

LEGEND_CHANCE = 1000000    # Make easier/harder
PLAYER_ENERGY = 100        # Starting energy
SEARCH_COST = 10           # Energy per search
FAME_REQUIRED = 1000       # Fame needed to win

📜 Credits

    ASCII art generated with patorjk.com

    Inspired by classic text adventures

🌟 Coming Soon

    More legendary coders to find

    Special power-ups

    Global leaderboard
