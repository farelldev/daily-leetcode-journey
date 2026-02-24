class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {'}' : '{',
                ')' : '(',
                ']' : '['}
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            else:
                if stack and stack[len(stack)-1] == pair[s[i]]:
                    stack.pop()
                else: return False

        return not stack