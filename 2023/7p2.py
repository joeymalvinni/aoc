from collections import Counter

cards = [tuple(card.split()) for card in open(0).read().splitlines()]
card_map = {"T": "B", "J": "0", "Q": "C", "K": "D", "A": "E"}

# sort weakest to be first

def strength(card):
    hand, bid = card

    counter = Counter(hand)
    print(counter)

    if "0" in hand and not counter["0"] == 5:
        elements = {i:counter[i] for i in counter if i != "0"}
        print(elements)
        for x in range(counter["0"]):
            counter[max(elements, key=elements.get)] += 1

            del counter["0"]

        items = sorted(counter.values())

        if items == [1, 1, 1, 1, 1]:
            return (1, hand)
        elif items == [1, 1, 1, 2]:
            return (2, hand)
        elif items == [1, 2, 2]:
            return (3, hand)
        elif items == [1, 1, 3]:
            return (4, hand)
        elif items == [2, 3]:
            return (5, hand)
        elif items == [1, 4]:
            return (6, hand)
        elif items == [5]:
            return (7, hand)

cards = [("".join([card_map.get(x[0], x[0]) for x in i[0]]), int(i[1])) for i in cards]

cards.sort(key=lambda x: strength(x))

total = 0

for i, card in enumerate(cards):
    hand, bid = card

    total += bid * (i+1)

print(total)
