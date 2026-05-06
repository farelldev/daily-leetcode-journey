class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {'+','-','*','/'}

        for i in tokens:
            if i not in operator:
                stack.append(int(i))

            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if i == "+": stack.append(num1 + num2)
                if i == "-": stack.append(num1 - num2)
                if i == "*": stack.append(num1 * num2)
                if i == "/": stack.append(int(num1 / num2))

        return stack[0]