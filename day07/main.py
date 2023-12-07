from enum import Enum

CARDS = "AKQJT98765432"
PART2_CARDS = "AKQT98765432J"

class Hand:
    def __init__(self, cards):
        self.cards = cards
        counts = {c: cards.count(c) for c in set(cards)}
        self.sorted_cards = sorted(
            [(card, count) for card, count in counts.items()],
            key = lambda k: (k[1], CARDS.index(k[0]) * -1),
            reverse=True,
        )

    def __lt__(self, other):
        for i, (card, count) in enumerate(self.sorted_cards):
            other_card, other_count = other.sorted_cards[i]
            if count > other_count:
                return True
            if count < other_count:
                return False
        for i, c in enumerate(self.cards):
            if CARDS.index(c) < CARDS.index(other.cards[i]):
                return True
            if CARDS.index(c) > CARDS.index(other.cards[i]):
                return False
        return False

    def __repr__(self):
        return str(self.sorted_cards)
    
class Hand2:
    def __init__(self, cards):
        self.cards = cards
        counts = {c: cards.count(c) for c in set(cards)}
        if (j_count := counts.get("J")):
            if j_count == 5:
                counts = {"A": 5}
            else:
                del counts["J"]
                sorted_counts = sorted(
                    [(card, count) for card, count in counts.items()],
                    key = lambda k: (k[1], CARDS.index(k[0]) * -1),
                    reverse=True,
                )
                counts[sorted_counts[0][0]] += j_count
            
        self.sorted_cards = sorted(
            [(card, count) for card, count in counts.items()],
            key = lambda k: (k[1], PART2_CARDS.index(k[0]) * -1),
            reverse=True,
        )



    def __lt__(self, other):
        for i, (card, count) in enumerate(self.sorted_cards):
            other_card, other_count = other.sorted_cards[i]
            if count > other_count:
                return True
            if count < other_count:
                return False
        for i, c in enumerate(self.cards):
            if PART2_CARDS.index(c) < PART2_CARDS.index(other.cards[i]):
                return True
            if PART2_CARDS.index(c) > PART2_CARDS.index(other.cards[i]):
                return False
        return False

    def __repr__(self):
        return str(self.sorted_cards)


lines = open('input.txt').read().split("\n")
data = []
data2 = []
for line in lines:
    hand, bid = line.split(" ")
    data.append((Hand(hand), int(bid)))
    data2.append((Hand2(hand), int(bid)))

def part1(data):
    ranks = sorted(data)
    return sum(bid * (len(ranks) - i) for i, (_, bid) in enumerate(ranks))

def part2(data):
    ranks = sorted(data)
    return sum(bid * (len(ranks) - i) for i, (_, bid) in enumerate(ranks))
        

print(part1(data))
print(part2(data2))