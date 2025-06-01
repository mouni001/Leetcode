class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in {"+", "-", "/","*"}:
                stack.append(int(token))
            else:
                number1 = stack.pop()
                number2 = stack.pop()
                if token == "+":
                    res = number2 + number1
                elif token == "-":
                    res = number2 - number1
                elif token == "*":
                    res = number2 * number1
                elif token == "/":
                     res = int(number2 / number1)
                stack.append(res)
        return stack.pop()
