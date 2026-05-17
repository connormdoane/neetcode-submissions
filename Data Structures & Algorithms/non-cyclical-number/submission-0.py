class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)
        while True:
            n = sum([int(i)**2 for i in str(n)])
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
        