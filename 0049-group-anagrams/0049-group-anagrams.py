class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pair = {}
        res = []
        
        for word in strs:
            freq = [0] * 26

            for lett in word:
                freq[ord(lett) - 97] += 1
            freq = tuple(freq)

            if freq not in pair:
                pair[freq] = [word]
            else:
                pair[freq].append(word)
        
        for key in pair:
            res.append(pair[key])

        return res