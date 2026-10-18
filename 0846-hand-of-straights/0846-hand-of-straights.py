class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        hand = sorted(hand)

        while len(hand) != 0:
            smallest = hand[0]
            hand.remove(smallest)

            for _ in range(groupSize - 1):
                smallest += 1

                if smallest not in hand: return False
                hand.remove(smallest)

        return True