class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        res = 1
        chars = set()

        l, r = 0, 0
        chars.add(s[l])
        valid = True
        while r != len(s)-1 or not valid:
            if valid and r != len(s)-1:
                r += 1
                if s[r] in chars:
                    valid = False
                    continue
                res = max(res, r-l+1)
                chars.add(s[r])
                continue
            if not valid:
                if s[l] == s[r]:
                    valid = True
                    l += 1
                    continue
                chars.remove(s[l])
                l += 1
        return res
