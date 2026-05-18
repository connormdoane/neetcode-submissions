class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        data = []
        for c in tokens:
            if c not in "+-*/": # number
                data.append(int(c))
            else:
                op2 = data.pop()
                op1 = data.pop()
                if c == "+":
                    data.append(op1 + op2)
                elif c == "-":
                    data.append(op1 - op2)
                elif c == "*":
                    data.append(op1 * op2)
                elif c == "/":
                    data.append(op1 // op2)
        return data.pop()
