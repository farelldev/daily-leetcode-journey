class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        hand = sorted(hand)
        freq = {i : 0 for i in hand}
        for i in hand: freq[i] += 1

        for i in hand:
            if freq[i] == 0: continue

            smallest = i
            for i in range(groupSize):
                if smallest not in freq or freq[smallest] == 0: return False

                freq[smallest] -= 1
                smallest += 1

        return True