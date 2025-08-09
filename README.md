# 🎰 Python Slot Machine

A terminal-based slot machine game made with Python.  
Spin the reels, place your bets, and win based on matching colorful emojis!  
Symbols include: 🍍, 🍇, 🥕, 🥑, 🍎

---

## 🚀 Features

- Spin a 3-symbol slot machine with emoji symbols
- Win real-time rewards based on matching symbols
- Track total spins, wins, and win rate
- All spins are logged in slot_log.csv with full details
- Simple, interactive, beginner-friendly CLI game

---

## 🎮 Symbols & Payouts

If all 3 symbols match, you win a multiplier based on the emoji:

| Symbol | Multiplier |
|--------|------------|
| 🍍     | x3         |
| 🍇     | x5         |
| 🥕     | x10        |
| 🥑     | x20        |
| 🍎     | x30        |

---

## 🧾 Game Log: slot_log.csv

Each spin is recorded in a CSV file with the following columns:

- Timestamp
- Spin #
- Symbol 1, 2, 3
- Bet
- Payout
- Net Change
- Initial Balance
- Final Balance
- Result (Same / Different)
- Winning Symbol (if applicable)

---

## ▶️ How to Play

### 1. Clone the repo or download the .py file  
### 2. Run it with Python:

`bash
python slot_machine.py

## 🖥️ Terminal Output

Here's a sample run of the Python Slot Machine in the terminal:

![Terminal Output](https://github.com/Ampika-Maity/slot-machine-python/blob/main/Screenshots/terminal_running_output.png)

---

## 📊 CSV Log Output

This is how the slot_log.csv output looks after a few spins:

![CSV Output](https://github.com/Ampika-Maity/slot-machine-python/blob/main/Screenshots/CSV_preview.png)

----
## 🎰 Dashboard Workflow

Here's the dashboard of the game (Final Output) :

![Dashboard_overview](https://github.com/Ampika-Maity/slot-machine-python/blob/main/Screenshots/slot_machine_dashboard.png)
