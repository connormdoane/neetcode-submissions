class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = 2
        for i in range(n):
            for num in nums:
                ans.append(num)
        return ans