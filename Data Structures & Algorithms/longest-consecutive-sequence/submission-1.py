class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        res = 0

        for i in s:
            if i-1 in s:
                continue
            # We're at a starting value, check the size of the set
            c = 1
            n = i+1
            while n in s:
                c += 1
                n += 1
            res = max(res, c)
            
        return res