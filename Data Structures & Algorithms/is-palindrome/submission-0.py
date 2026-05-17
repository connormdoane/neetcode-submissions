class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        f = [c.lower() for c in s if c.lower() in alphabet]
        for i in range(len(f)):
            if f[i] != f[len(f)-i-1]:
                return False
        return True