class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = False
        hashset = set()
        for num in nums:
            if num not in hashset:
                hashset.add(num)
            else:
                ans = True
        return ans
        #O(n)