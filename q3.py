import random

suits = "♠♥♣♦"
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# Make a deck of cards
deck = []
for suit in suits:
    for value in values:
        deck.append(value + suit)

# Shuffle the deck
random.shuffle(deck)

# Sample a hand of 5 cards (without replacement)
hand = random.sample(deck, 5)

# Print the shuffled deck and the hand
print("Shuffled Deck:")
print(deck)

print("\nHand:")
print(hand)