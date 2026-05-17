class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre = [1 for i in nums] # Will store all left-side mult values
        suf = [1 for i in nums] # All right-side mult values
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1] # Get value based on prev pre, not all prev values
        for i in range(len(nums)-2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1] # Be sure to not include Self

        for i in range(len(nums)): # Now just multiply the left half and right half
            res.append(pre[i] * suf[i])

        return res