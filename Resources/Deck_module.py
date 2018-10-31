from random import shuffle


class Deck:

    suits = ["Diamonds", "Spades", "Clubs", "Hearts"]
    cards = {
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
        "Six": 6,
        "Seven": 7,
        "Eight": 8,
        "Nine": 9,
        "Ten": 10,
        "Jack": 10,
        "Queen": 10,
        "King": 10,
        "Ace": 11
    }

    def __init__(self, decks=1, deckcards=[]):
        """
        :param decks: Specify how many decks to create and shuffle. Default is 1 deck
        :param deckcards: Specify specific cards to shuffle each card has the syntax like follows
        ["Diamond", "Six", "6"] and decks argument has to be 0 to work
        """
        self.decks = decks
        self.deckcards = deckcards

    def create_a_deck(self):

        # Creates a deck of cards according to how many decks the user specifies(default is one deck).
        for deck in range(self.decks):
            for suit in self.suits:
                for card in self.cards:
                    self.deckcards.append(suit + " " + card + " " + f"{self.cards[card]}")
        shuffle(self.deckcards)
        shuffle(self.deckcards)
        shuffle(self.deckcards)

    def hit(self):

        # Picks the first card from the created deck without returning it.
        if len(self.deckcards) != 0:
            card = self.deckcards[0]
            self.deckcards.pop(0)
            splitcard = card.split()
            # print("Your card is: " + splitcard[1] + " of " + splitcard[0])
            # print(int(splitcard[2]))
            return splitcard
        else:
            self.create_a_deck()
            card = self.deckcards[0]
            self.deckcards.pop(0)
            splitcard = card.split()
            # print("Your card is: " + splitcard[1] + " of " + splitcard[0])
            # print(int(splitcard[2]))
            return splitcard

    def __str__(self):
        return f"{self.deckcards}"


