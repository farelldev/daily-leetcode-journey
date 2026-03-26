class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sell = prices[0]
        prof = maxProf = j = 0

        for i in range(len(prices)):
            sell = prices[i]
            
            while buy > sell:
                j += 1
                buy = prices[j]
            prof = sell - buy

            maxProf = max(maxProf, prof)

        return maxProf