class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False

        hand.sort()
        freq = Counter(hand)

        for card in hand:
            if freq[card] == 0: continue

            for value in range(card, card + groupSize):
                if freq[value] == 0:
                    return False

                freq[value] -= 1

        return True