class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        start = 0
        end = len(s)-1
        while start < end:
            if s[start].lower() not in alphabet:
                start += 1
                continue
            if s[end].lower() not in alphabet:
                end -= 1
                continue
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True