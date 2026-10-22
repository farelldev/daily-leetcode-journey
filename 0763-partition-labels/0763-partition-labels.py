class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = defaultdict(int)
        res = []
        
        for i in range(len(s)):
            last[s[i]] = i

        current = furthest = 0
        for i in range(len(s)):
            current += 1
            
            if furthest < last[s[i]]: furthest = last[s[i]]

            if i == furthest:
                res.append(current)
                current = 0

        return res
