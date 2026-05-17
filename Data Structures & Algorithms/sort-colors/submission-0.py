class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0 = 0
        count2 = 0
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 2:
                count2 += 1
        for i in range(len(nums)):
            if i < count0:
                nums[i] = 0
            elif i > len(nums) - count2 -1:
                nums[i] = 2
            else:
                nums[i] = 1