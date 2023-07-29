from dataclasses import dataclass
import random

from init_cards import init_cards

@dataclass
class Cards:
    cards: list

    def shuffle(self):
        random.shuffle(self.cards)


class Hand:
    def __init__(self):
        ...



def main():
    # 1. Initialize random order of cards
    # 2. Split cards to two players
    # 3. Assign values to each card
    # Until there are cards:
    # 1. Count the cards for each player
    # 2. Print the cards of each player
    # 3. Compare the two cards
    # 4. Give away cards to player, who won the round
    cards = Cards(cards = init_cards())
    cards.shuffle()
    print(cards)


if __name__ == "__main__":
    main()
