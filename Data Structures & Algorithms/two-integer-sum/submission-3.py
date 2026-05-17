class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = {}
        for i,n in enumerate(nums):
            if target-n in l:
                return [l[target-n],i]
            l[n] = i