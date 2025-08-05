# Python Slot Machine
import random
import csv
from datetime import datetime

def spin_row():
    symbols = ["🍍", "🍇", "🥕", "🥑", "🍎"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("****")
    print("|".join(row))
    print("****")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍍":
            return bet * 3
        elif row[0] == "🍇":
            return bet * 5
        elif row[0] == "🥕":
            return bet * 10
        elif row[0] == "🥑":
            return bet * 20
        elif row[0] == "🍎":
            return bet * 30
    return 0

def log_spin(spin_number, row, bet, payout, initial_balance, final_balance):
    file_exists = False
    try:
        with open("slot_log.csv", "r", encoding="utf-8"):
            file_exists = True
    except FileNotFoundError:
        pass

    with open("slot_log.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow([
                "Timestamp", "Spin #", "Symbol 1", "Symbol 2", "Symbol 3",
                "Bet", "Payout", "Net Change", "Initial Balance", "Final Balance", "Result", "Winning Symbol"
            ])

        result = "Same" if row[0] == row[1] == row[2] else "Different"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        net_change = payout - bet
        winning_symbol = row[0] if result == "Same" else ""

        writer.writerow([
            timestamp, spin_number, *row, bet, payout, net_change,
            initial_balance, final_balance, result, winning_symbol
        ])

def main():
    balance = 100
    spin_number = 1
    total_wins = 0
    total_spins = 0

    print("******************")
    print("Welcome to Python Slot Machine")
    print("Symbols: 🍍 🍇 🥕 🥑 🍎")
    print("******************")

    while balance > 0:
        print(f"Current Balance is : ₹{balance}")
        bet = input("Enter your bet amount (or type 'exit' to quit): ₹")
        if bet.lower() == "exit":
            print("Thanks for playing! 🎉")
            break
        if not bet.isdigit():
            print("Please enter a valid ✅ number")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient Balance ⚠️")
            continue
        if bet <= 0:
            print("Bet must be greater than ZERO ⚠️")
            continue

        initial_balance = balance
        balance -= bet

        row = spin_row()
        print("Spinning....\n")
        print_row(row)

        payout = get_payout(row, bet)
        total_spins += 1

        if payout > 0:
            print(f"You won 🤩 ₹{payout}")
            total_wins += 1
        else:
            print("Sorry 😥!! You lost this round")

        balance += payout

        win_percentage = (total_wins / total_spins) * 100
        print(f"📊 Total Spins: {total_spins}, Wins: {total_wins}, Win Rate: {win_percentage:.2f}%")

        log_spin(spin_number, row, bet, payout, initial_balance, balance)
        spin_number += 1

if __name__ == "__main__":  
    main()