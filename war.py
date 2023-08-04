from dataclasses import dataclass
import random
import numpy as np

from init_cards import init_cards

@dataclass
class Cards:
    cards: list

    def shuffle(self):
        random.shuffle(self.cards)

    def split(self, player_count):
        # len_of_cards = len(self.cards)
        # first = self.cards[int(len(self.cards)/2):]
        # second = self.cards[:int(len(self.cards)/2)]
        return np.array_split(self.cards, player_count)
        # return first, second


class Hand:
    def __init__(self, cards):
        self.cards = cards
        print(cards)

    # def get_hand(self, split_array):




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
    player_count = int(input("How many players do you have? "))
    split_array = cards.split(player_count)
    for array in split_array:
        hand = Hand(array)
    # handPlayer = Hand(hand1)
    # handComputer = Hand(hand2)
    # print(hand1)
    # print(hand2)


if __name__ == "__main__":
    main()
