import random
# card
# suit, rank, value,
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
         'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


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


# player
class Player:

    def __init__(self, name):

        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
#for a in new_deck.all_cards:
#    print(a)
new_deck.shuffle()
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

#print(player_one)
#print(player_two)
game_on = True
round_num = 0

while game_on:

    round_num += 1
    print(f"Round {round_num}")

    if len(player_two.all_cards) == 0:
        print('Player One, out of cards! Player Two wins')
        game_on = False
        break

    if len(player_one.all_cards) == 0:
        print('Player Two, out of cards! Player One wins')
        game_on = False
        break

    player_one_cards = []
    player_two_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:
        """print(f"Player 1: {player_one} vs Player 2: {player_two}")
        print(f"Player 1: {player_one_cards[-1]} vs. Player 2: {player_two_cards[-1]}")
        try:
            player_one_cards[-1].value
        except:
            print(player_one_cards[-1])
        try:
            player_two_cards[-1].value
        except:
            print(player_two_cards[-1])"""
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        else:
            print("WAR!")

            if len(player_one.all_cards) < 5:
                print("Player One unable to declare war")
                print("PLAYER TWO WINS!")
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print("Player Two unable to declare war")
                print("PLAYER ONE WINS!")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())