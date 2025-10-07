import random
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

# Load basic strategy from CSV
df = pd.read_csv("blackjack_book.csv")

deck_size = 6  # Number of standard decks in the shoe
base_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4 * deck_size

shoe_data = []

starting_money = 10000000
money = starting_money
initial_initial_bet = 100
initial_bet = initial_initial_bet
bet_strategy = "flat"
insurance = False  # TODO: add insurance


def shuffle_deck():
    action_deck = base_deck.copy()
    random.shuffle(action_deck)
    return action_deck


def deal_card(deck, hand):
    card = deck.pop()
    hand.append(card)
    return card


def read_hand_strategy(player_hand, dealer_card):
    if len(player_hand) == 2 and player_hand[0] == player_hand[1]:
        row = df[df["bk"] == "p" + str(player_hand[0])]
    elif 11 in player_hand:
        row = df[df["bk"] == "a" + str(sum(player_hand) - 11)]
    else:
        row = df[df["bk"] == str(sum(player_hand))]
    if row.empty:
        return "S"  # Default action if no strategy found
    action = row[str(dealer_card)].values[0]
    return action


def calculate_bet_strategy(strategy, lpw, prev_bet, money):
    if strategy == "flat":
        return min(initial_bet, money)
    elif strategy == "martingale":
        if lpw == 1:
            print("martingale bet: " + str(initial_bet))
            return initial_bet
        elif lpw == 0:
            print("martingale bet: " + str(prev_bet))
            return prev_bet
        else:
            print("martingale bet: " + str(min(prev_bet * 2, money)))
            return min(prev_bet * 2, money)
    elif strategy == "1326":
        if lpw == 1:
            if prev_bet == initial_bet:
                return min(initial_bet * 3, money)
            elif prev_bet == initial_bet * 3:
                return min(initial_bet * 2, money)
            elif prev_bet == initial_bet * 2:
                return min(initial_bet * 6, money)
            else:
                return min(initial_bet, money)
        elif lpw == 0:
            return prev_bet
        else:
            return min(initial_bet, money)
    elif strategy == "dad":
        if lpw == 1:
            return min(prev_bet * 1.5, money)
        elif lpw == 0:
            return prev_bet
        else:
            return min(initial_bet, money)
    elif strategy == "ai-generated":
        if lpw == 1:
            return max(initial_bet, prev_bet - initial_bet)
        elif lpw == 0:
            return prev_bet
        else:
            return min(prev_bet + initial_bet, money)
    elif strategy == "hi-lo":
        # Placeholder for hi-lo card counting strategy
        return min(initial_bet, money)
    elif strategy == "random":
        return min(random.randint(initial_bet, min(initial_bet * 5, money)), money)
    else:
        return min(initial_bet, money)


def hand(
    deck,
    money,
    bet,
    player_hand=[],
    dealer_hand=[],
    dealer_card=None,
    insurance=False,
    split=False,
):
    if len(player_hand) == 0 and not split:
        deal_card(deck, player_hand)
        dealer_card = deal_card(deck, dealer_hand)
        deal_card(deck, player_hand)
        deal_card(deck, dealer_hand)

        insurance_bet = 0

        if dealer_card == 11 and insurance and not (money < int(bet / 2)):
            insurance_bet = int(bet / 2)
            money -= insurance_bet

        if insurance and sum(dealer_hand) == 21:
            print("insurance pays")
            money += 2 * insurance_bet
        elif insurance and insurance_bet != 0:
            print("insurance loses")

        if sum(player_hand) == 21 and sum(dealer_hand) != 21:
            money += int(1.5 * bet)
            print("p win with blackjack, bet: " + str(bet))
            return 1, money
        elif sum(dealer_hand) == 21 and sum(player_hand) != 21:
            money -= bet
            print("dealer blackjack, bet: " + str(bet))
            return -1, money
        elif sum(dealer_hand) == 21 and sum(player_hand) == 21:
            print("push, bet: " + str(bet))
            return 0, money

    dealer_card = dealer_hand[0]
    if dealer_card == 1:
        print("dealer 1?")
        print(dealer_hand)

    action = read_hand_strategy(player_hand, dealer_card)
    while not (action == "S"):
        if action == "H":
            deal_card(deck, player_hand)
            if sum(player_hand) > 21 and 11 in player_hand:
                player_hand[player_hand.index(11)] = 1
            if sum(player_hand) > 21:
                money -= bet
                print("p bust, bet: " + str(bet))
                return -1, money
        elif action == "D":
            if money < bet * 2:
                action = "H"
                continue
            else:
                bet *= 2
                print("bet doubled, bet: " + str(bet))
            deal_card(deck, player_hand)
            if sum(player_hand) > 21 and 11 in player_hand:
                player_hand[player_hand.index(11)] = 1
            if sum(player_hand) > 21:
                money -= bet
                print("p bust, bet: " + str(bet))
                return -1, money
            break
        elif action == "P":
            if money < bet * 2:
                action = "H"
                continue

            print("split, bet: " + str(bet))

            # Create new hands for splitting
            new_hand1 = [player_hand[0]]
            new_hand2 = [player_hand[1]]
            deal_card(deck, new_hand1)
            deal_card(deck, new_hand2)

            result1, money = hand(
                deck, money, bet, new_hand1, dealer_hand, dealer_card, insurance, True
            )
            result2, money = hand(
                deck, money, bet, new_hand2, dealer_hand, dealer_card, insurance, True
            )

            return result1 + result2, money
        action = read_hand_strategy(player_hand, dealer_card)

    while sum(dealer_hand) < 17:
        deal_card(deck, dealer_hand)
        if sum(dealer_hand) > 21 and 11 in dealer_hand:
            dealer_hand[dealer_hand.index(11)] = 1
        if sum(dealer_hand) > 21:
            money += bet
            print("hand won, bet: " + str(bet))
            return 1, money
    if sum(player_hand) > sum(dealer_hand):
        money += bet
        print("hand won, bet: " + str(bet))
        return 1, money
    elif sum(player_hand) == sum(dealer_hand):
        print("push, bet: " + str(bet))
        return 0, money
    else:
        money -= bet
        print("hand lost, bet: " + str(bet))
        return -1, money

    # should never reach here
    return 2, money


def shoe(money, bet_strategy=bet_strategy, insurance=insurance):
    global initial_bet
    if money <= 0:
        print("run out of money.")
        return money
    deck = shuffle_deck()
    prev_hand, money = hand(deck, money, initial_bet, [], [], None, insurance)
    shoe_data.append(money)
    print("current money: " + str(money))
    prev_bet = initial_bet
    initial_bet = initial_initial_bet
    while (len(deck)) > len(base_deck) / 4:
        prev_bet = calculate_bet_strategy(bet_strategy, prev_hand, prev_bet, money)
        prev_hand, money = hand(deck, money, prev_bet, [], [], None, insurance)
        print("hand complete, cards left in shoe: " + str(len(deck)))
        shoe_data.append(money)
        print("current money: " + str(money))
        if money <= 0:
            print("run out of money.")
            return money
    print("Shoe complete, reshuffling")
    initial_bet = prev_bet
    return money


def main():
    """
    strategy = input("Enter bet strategy: ")
    if strategy not in ["flat", "martingale", "1326", "dad", "random"]:
        print("strategy undefined, try again")
        main()
        return
    if input("Do you take insurance? ") == "yes":
        insurance = True
    else:
        insurance = False
    shoes = int(input("Enter number of shoes to simulate: "))
    """
    strategy = "martingale"
    insurance = False
    shoes = 5
    current_money = money
    for i in range(shoes):
        current_money = shoe(current_money, strategy, insurance)
        print(f"After shoe {i+1}, total money: {current_money}")
    if current_money <= starting_money:
        print("one additional shoe")
        current_money = shoe(current_money, strategy, insurance)
        print(f"After shoe {shoes+1}, total money: {current_money}")
    plt.plot(shoe_data)
    plt.show()
    print(f"Final money: {current_money}")


main()
