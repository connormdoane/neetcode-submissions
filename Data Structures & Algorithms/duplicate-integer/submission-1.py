class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = False
        sorted = nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                ans = True
        return ans
        # O(nlogn)