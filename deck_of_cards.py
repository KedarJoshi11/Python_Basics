class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __repr__(self):
		return f"{self.value} of {self.suit}"

# c = Card("Ace", "hearts")
# c1 = Card("10", "Diamonds")
# c2 = Card("King", "Spades")
# print(c, c1, c2)

class Deck:
	def __init__(self):
		suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
		values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
		self.cards = [Card(value, suit) for suit in suits for value in values]
		

	def __repr__(self):
		return f"Deck of {self.count()} cards"

	def count(self):
		return len(self.cards)

	def _deal(self, num):
		count = self.count()
		actual = min([count, num])
		print(f"Going to remove {actual} cards")
		if count == 0:
			raise ValueError("All cards have been dealt!")
		cards = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		return cards

	def deal_card(self):
		return self._deal(1)[0]

	def deal_hand(self, num):
		return self._deal(hand_size)

	def shuffle(self):
		if self.count < 52:
			raise ValueError("Only full decks can be shuffled!")
		shuffel(self.cards) 



d = Deck()
d.shuffle()
print(d.cards)