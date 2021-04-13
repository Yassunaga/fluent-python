import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = '0 1'.split()

    def __init__(self):
        self.cards = [
            str(rank + suit + rank2)
            for rank in self.ranks
            for suit in self.ranks
            for rank2 in self.ranks
        ]

    def __getitem__(self, position):
        return self.cards[position]

    def __len__(self):
        return len(self.cards)


a = FrenchDeck()
print(a.cards)
