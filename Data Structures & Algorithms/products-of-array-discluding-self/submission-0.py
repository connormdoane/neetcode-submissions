class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre = [1 for i in nums]
        suf = [1 for i in nums]
        for i in range(1, len(nums)): # Calculate prefix products
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]
        for i in range(len(nums)):
            res.append(pre[i] * suf[i])

        return res