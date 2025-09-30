import random
import pandas as pd
import numpy as np
import csv

# Load basic strategy from CSV
df = pd.read_csv("blackjack_book.csv")

deck_size = 6  # Number of standard decks in the shoe
base_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4 * deck_size

money = 10000
initial_bet = 100
bet_strategy = "flat"  # flat / martingale / 1326 / dad / random
insurance = False


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
            return initial_bet
        elif lpw == 0:
            return prev_bet
        else:
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


def hand(deck, money, bet, player_hand=[], dealer_hand=[], dealer_card=None):
    if len(player_hand) == 0:
        deal_card(deck, player_hand)
        dealer_card = deal_card(deck, dealer_hand)
        deal_card(deck, player_hand)
        deal_card(deck, dealer_hand)

        if sum(player_hand) == 21 and sum(dealer_hand) != 21:
            money += int(1.5 * bet)
            print("hand won with blackjack")
            return 1
        elif sum(dealer_hand) == 21 and sum(player_hand) != 21:
            money -= bet
            return -1
        elif sum(dealer_hand) == 21 and sum(player_hand) == 21:
            return 0
        # run blackjack check here
        print("new not split hand")

    dealer_card = dealer_hand[0]

    action = read_hand_strategy(player_hand, dealer_card)
    while action not in ["S", "D"]:
        if action == "H":
            deal_card(deck, player_hand)
            if sum(player_hand) > 21 and 11 in player_hand:
                player_hand[player_hand.index(11)] = 1
            if sum(player_hand) > 21:
                money -= bet
                return -1
        elif action == "P":
            if money < bet * 2:
                action = "H"
                continue
            money -= bet
            hand(
                deck,
                money,
                bet,
                [player_hand[0], deal_card(deck, [])],
                dealer_hand,
                dealer_card,
            )
            hand(
                deck,
                money,
                bet,
                [player_hand[0], deal_card(deck, [])],
                dealer_hand,
                dealer_card,
            )
            return
        action = read_hand_strategy(player_hand, dealer_card)

    if action == "D":
        if not (money < bet * 2):
            money -= bet
            bet *= 2

        deal_card(deck, player_hand)
        if sum(player_hand) > 21 and 11 in player_hand:
            player_hand[player_hand.index(11)] = 1
        if sum(player_hand) > 21:
            money -= bet
            return -1

    while sum(dealer_hand) < 17:
        deal_card(deck, dealer_hand)
        if sum(dealer_hand) > 21 and 11 in dealer_hand:
            dealer_hand[dealer_hand.index(11)] = 1
        if sum(dealer_hand) > 21:
            money += bet
            print("hand won, bet: " + str(bet))
            return 1
    if sum(player_hand) > sum(dealer_hand):
        money += bet
        print("hand won, bet: " + str(bet))
        return 1
    elif sum(player_hand) == sum(dealer_hand):
        return 0
    else:
        money -= bet
        return -1

    return 2


def shoe(bet_strategy=bet_strategy, insurance=insurance):
    deck = shuffle_deck()
    prev_hand = hand(deck, money, initial_bet, [], [], None)
    prev_bet = initial_bet
    while (len(deck)) > len(base_deck) / 4:
        prev_bet = calculate_bet_strategy(bet_strategy, prev_hand, prev_bet, money)
        prev_hand = hand(deck, money, prev_bet, [], [], None)
        print("hand complete, cards left in shoe: " + str(len(deck)))
        print("current money: " + str(money))
    print("Shoe complete, reshuffling")
    return


def main():
    shoes = int(input("Enter number of shoes to simulate: "))
    for i in range(shoes):
        shoe()


main()
