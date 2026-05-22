class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in '[({':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                opener = stack.pop()
                if opener == '[' and ch != ']':
                    return False
                if opener == '{' and ch != '}':
                    return False
                if opener == '(' and ch != ')':
                    return False
        return stack == []
