class Solution:
    def findMin(self, nums: List[int]) -> int:
        p1 = 0
        p2 = len(nums)-1
        while p1 < p2:
            pivot = p1 + (p2-p1)//2
            if nums[pivot] < nums[p2]: # min in second half
                p2 = pivot
            else:
                p1 = pivot+1
        return nums[p1]