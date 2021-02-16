"""
Dobble is a game in which players have to find symbols in common between two cards.
It was the UK’s best-selling game in 2018 and 2019.
The game is sold as Dobble in Europe and Spot It! in the US. The name is a play on the word 'double'.

Key Properties:
1. Every card has exactly 8 symbols on it.
2. Every pair of cards share exactly one symbol in common.
3. No symbol appears on every card.
"""

import string
import random

symbol = []
symbol = list(string.ascii_letters)

card1 = [0] * 5
card2 = [0] * 5

# position1 and position2 are same symbol positions in card1 and card2, respectively
position1 = random.randint(0, 4)
position2 = random.randint(0, 4)

samesymbol = random.choice(symbol)
symbol.remove(samesymbol)  # so that no letter is repeated

if position1 == position2:
    card1[position1] = samesymbol
    card2[position2] = samesymbol
else:
    card1[position1] = samesymbol
    card2[position2] = samesymbol

    card1[position2] = random.choice(symbol)
    symbol.remove(card1[position2])
    card2[position1] = random.choice(symbol)
    symbol.remove(card2[position1])

i = 0
while i < 5:
    if i != position1 and i != position2:
        alphabet1 = random.choice(symbol)
        symbol.remove(alphabet1)
        alphabet2 = random.choice(symbol)
        symbol.remove(alphabet2)

        card1[i] = alphabet1
        card2[i] = alphabet2
    i = i + 1

print(*card1)
print(*card2)
print()
print("Spot it!")
ans = input("Enter your answer: ")
if ans == samesymbol:
    print("Right. Keep it up!")
else:
    print("Better luck next time.")
    print("Correct answer is ", samesymbol)
