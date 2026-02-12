class Solution:
    def isValid(self, s: str) -> bool:
        order = []
        pair = {'}' : '{',
                ')' : '(',
                ']' : '['}
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                order.append(s[i])
            else:
                if order and order[len(order)-1] == pair[s[i]]:
                    order.pop(len(order) - 1)
                else: return False

        return not order