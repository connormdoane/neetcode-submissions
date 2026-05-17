class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        ans = maxCount = 0

        for num in nums:
            count[num] += 1
            if maxCount < count[num]:
                ans = num
                maxCount = count[num]

        return ans
        # O(n)
        # O(n)