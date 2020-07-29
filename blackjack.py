import random
import os

# card
# suit, rank, value,
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
         'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# deck
class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the card object
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

    def shuffle(self):

        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


def dealer_deck():
    dealer = [new_deck.deal_one()]
    for d in dealer:
        print(f"Dealer has drawn: {d}\n")
    d_total = sum([a.value for a in dealer])
    return dealer, d_total, d


def player_deck():
    player = [new_deck.deal_one(), new_deck.deal_one()]
    for a in player:
        print(a)
    p_total = sum([a.value for a in player])
    print(f"Total: {p_total}")
    return player, p_total


def player_hit(player, d):
    print(f"Dealer has drawn: {d}\n")
    player.append(new_deck.deal_one())
    for a in player:
        print(a)
    p_total = sum([a.value for a in player])
    if p_total > 21 and "Ace" in [a.rank for a in player]:
        p_total -= 10
    print(f"Total: {p_total}")
    if p_total > 21:
        print("BUST!")
    return player, p_total


def dealer_round(dealer, p_total):
    d_total = sum([a.value for a in dealer])
    while d_total < p_total:
        dealer.append(new_deck.deal_one())
        d_total = sum([a.value for a in dealer])
        if d_total > 21:
            print("DEALER BUSTED!")
            break
    for a in dealer:
        print(a)
    print(d_total)
    return dealer, d_total


new_deck = Deck()
new_deck.shuffle()
balance = 100

while True:

    os.system('clear')
    print(f"Players balance: {balance}")
    if balance < 10:
        print("Player is out of money")
        quit()

    while True:

        bet = input("Place a bet, minimum bet is 10\n")
        if bet.isdigit() and balance >= int(bet) >= 10:
            bet = int(bet)
            break

    dealer, d_total, d = dealer_deck()
    player, p_total = player_deck()

    while True:

        if p_total > 21:
            break

        while True:

            if p_total > 21:
                break
            hit = input(f"(H)it or (S)tay?\n")
            if hit.upper() == "H" or hit.upper() == "S":
                break

        if hit.upper() == "H":
            os.system('clear')
            player, p_total = player_hit(player, d)
        elif hit.upper() == "S":
            print("Dealer's turn")
            break

    if p_total > 21:
        print("Dealer wins")
        balance -= bet
    else:
        dealer, d_total = dealer_round(dealer, p_total)
        if d_total > 21:
            print("Player wins")
            balance += bet
        elif d_total >= p_total:
            print("Dealer wins")
            balance -= bet
        else:
            print("Player wins")
            balance += bet

    print(f"Player: {p_total} vs Dealer: {d_total}")

    while True:

        again = input("Play again? [Y/N]")
        if again.upper() == "Y" or again.upper() == "YES":
            break
        if again.upper() == "N" or again.upper() == "NO":
            print(f"Player has left the game with {balance}\nBye loser")
            quit()
