class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = set()
        for i in nums:
            if i not in res:
                res.add(i)
            elif i in res:
                res.remove(i)
        return list(res)[0]