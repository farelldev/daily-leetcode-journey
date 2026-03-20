class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = []

        for i in s:
            if i.isdigit(): clean.append(i)
            if i.isalpha(): clean.append(i.lower())

        return clean == clean[::-1]