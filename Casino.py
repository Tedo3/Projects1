import time
import random
import pygame

coins = 100
games = ["roulette", "ruletka", "slots", "rotativki"]
with open("games.txt", "w") as f:
    f.write(",".join(games))

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("mixkit-payout-award-1934.wav")


def loading():
    print("Loading.", end="")
    time.sleep(2)
    print("...", end="")
    time.sleep(1.5)
    print("......", end="")
    time.sleep(1)
    print(".........")
    time.sleep(0.5)
    return


def betting():
    global coins
    try:
        bet = int(input("Enter the amount you want to bet: "))
        if bet > coins:
            print("You don't have enough money.")
            return None
        elif bet <= 0:
            print("The bet must be a positive number.")
            return None
        print(f"You have bet {bet} lv, good luck!")
        if coins < 0:
            print("You have no money")
            exit()
        return bet
    except ValueError:
        print("The bet must be a number!")
        return None


print("===================================================================================================================")
print(
    "Welcome to CasinoBet. You can choose a game between Slots or Roulette.\n"
    "You can double your money or lose everything.\n"
    "Be careful, gambling can be addictive.\n"
    "Type Stop to exit the game. Have fun!"
)
print("===================================================================================================================")
print()
print("Available games:")
with open("games.txt", "r") as ri:
    print(ri.read())

while True:
    time.sleep(3)
    game = input("Enter the game you want to play: ")

    if game.lower() not in games:
        print("Choose one of the available games and try again!")
        continue
    else:
        break

if game in {"slots", "rotativki"}:
    win_coins = 0
    symbols = {
        "🍒": 10,
        "🍋": 20,
        "🍇": 30,
        "🔔": 50,
        "7️⃣": 100,
        "⭐": 200,
    }
    loading()
    print("Good choice. You start with 100 lv. You can hit the jackpot or lose everything. Bet wisely.")
    print()

    current_bet = None
    while current_bet is None:
        current_bet = betting()

    while True:
        action = input(
            "Press Enter to spin, type Stop to quit, type Change to change bet, or type Balance to see your money: "
        )

        if action.lower() in {"stop"}:
            print("Thanks for playing! Remaining money:", coins)
            break
        elif action.lower() in {"change"}:
            new_bet = betting()
            if new_bet is not None:
                current_bet = new_bet
                print(f"Remaining balance: {coins}")
        elif action.lower() in {"balance"}:
            print(f"You have {coins} lv.")
        else:
            try:
                if current_bet > coins:
                    print("Not enough money. Change your bet or stop.")
                    current_bet = betting()
            except TypeError:
                current_bet = betting()

            try:
                coins -= current_bet
                sound.play()
                spin = [random.choice(list(symbols.keys())) for _ in range(4)]
                time.sleep(2)
                print("============")
                print("|".join(spin))
                print("============")
            except TypeError:
                print("You must place a bet first.")

            if spin[0] == spin[1] == spin[2] == spin[3]:
                print("JACKPOT!!!")
                if spin[0] == "🍒":
                    win_coins = 10 * 10
                if spin[0] == "🍋":
                    win_coins = 20 * 10
                if spin[0] == "🍇":
                    win_coins = 30 * 10
                if spin[0] == "🔔":
                    win_coins = 50 * 10
                if spin[0] == "7️⃣":
                    win_coins = 100 * 10
                if spin[0] == "⭐":
                    win_coins = 200 * 10
                coins += win_coins

            for el in range(len(spin) - 3):
                if spin[el] == spin[el + 1] == spin[el + 2] or spin[el + 1] == spin[el + 2] == spin[el + 3]:
                    print("You got 3 in a row!")
                    if spin[el] == "🍒":
                        win_coins = 10 * 5
                    if spin[el] == "🍋":
                        win_coins = 20 * 5
                    if spin[el] == "🍇":
                        win_coins = 30 * 5
                    if spin[el] == "🔔":
                        win_coins = 50 * 5
                    if spin[el] == "7️⃣":
                        win_coins = 100 * 5
                    if spin[el] == "⭐":
                        win_coins = 200 * 5
                    coins += win_coins

                elif spin[el] == spin[el + 1] or spin[el + 1] == spin[el + 2] or spin[-2] == spin[-1]:
                    print("You doubled your win!")
                    if spin[el] == "🍒":
                        win_coins = 10 * 2
                    if spin[el] == "🍋":
                        win_coins = 20 * 2
                    if spin[el] == "🍇":
                        win_coins = 30 * 2
                    if spin[el] == "🔔":
                        win_coins = 50 * 2
                    if spin[el] == "7️⃣":
                        win_coins = 100 * 2
                    if spin[el] == "⭐":
                        win_coins = 200 * 2
                    coins += win_coins
                    print(f"Current balance: {coins} lv.")
                    print()

elif game in {"roulette", "ruletka"}:
    coins = 100
    current_bet = None
    numbers = {
        "red": [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36],
        "black": [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35],
        "green": [0]
    }

    loading()
    print("You start with 100 lv. Bet wisely.")

    while current_bet is None:
        current_bet = betting()

    while True:
        action = [el for el in input(
            "Bet on color (red/black/green), even/odd, and number (0-36), separated by comma. Type Stop to quit or Change to change bet: "
        ).lower().split(",")]

        if action[0] in {"stop"}:
            print(f"Thanks for playing! Remaining money: {coins} lv.")
            break

        if action[0] in {"change"}:
            new_bet = betting()
            if new_bet is not None:
                current_bet = new_bet
            continue

        if len(action) != 3:
            print("You must enter color, even/odd, and number!")
            continue

        bet_colour, bet_even_odd, bet_number = action

        try:
            bet_number = int(bet_number)
            if bet_number < 0 or bet_number > 36:
                raise ValueError
        except ValueError:
            print("Invalid number.")
            continue

        if coins < current_bet:
            print("Not enough money.")
            continue

        coins -= current_bet
        spin_number = random.randint(0, 36)

        if spin_number in numbers["red"]:
            spin_colour = "red"
        elif spin_number in numbers["black"]:
            spin_colour = "black"
        else:
            spin_colour = "green"

        if spin_number == 0:
            spin_even_odd = "zero"
        elif spin_number % 2 == 0:
            spin_even_odd = "even"
        else:
            spin_even_odd = "odd"

        print("------------------------------------------------")
        print(f"Result: {spin_colour}, {spin_even_odd}, {spin_number}")
        print("------------------------------------------------")

        win = 0
        if bet_colour == spin_colour:
            print("Correct color!")
            win += current_bet * 3
        if bet_even_odd == spin_even_odd:
            print("Correct even/odd!")
            win += current_bet * 3
        if bet_number == spin_number:
            print("Correct number!")
            win += current_bet * 7

        coins += win
        print(f"Current balance: {coins} lv.")
        print()

        if coins <= 0:
            print("Game over! You ran out of money.")
            break















