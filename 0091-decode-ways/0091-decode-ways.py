class Solution:
    def numDecodings(self, s: str) -> int:
        canHasTens = False
        foundZero = False
        l, r = 1, 0
        res = 1

        for i in range(len(s) - 1, -1, -1):
            if canHasTens and (s[i] == '1' or (s[i] == '2' and 0 <= int(s[i+1]) <= 6)):
                res = r + l
                canHasTens = False
                print("kena sini")

            if s[i] == '0':
                if foundZero or i == 0: return 0
                foundZero = True
                canHasTens = False
                res = 0

            elif foundZero:
                if s[i] > '2': return 0
                res = r
                foundZero = False
                canHasTens = True
                print("masuk foundzero")

            else:
                canHasTens = True

            r = l
            l = res

            print(s[i], res, l, r)

        return res