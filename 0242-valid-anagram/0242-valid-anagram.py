class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter = {}

        for i in s:
            if i not in letter:
                letter[i] = 1
            else:
                letter[i] += 1

        for i in t:
            if i not in letter or letter[i] == 0: 
                return False
            else:
                letter[i] -= 1

        return sum(letter.values()) == 0