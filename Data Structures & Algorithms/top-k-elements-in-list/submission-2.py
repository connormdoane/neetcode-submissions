class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di = {}
        output = []
        for i in nums:
            if i in di:
                di[i] += 1
            else:
                di[i] = 1
        s = sorted(di, key=di.get, reverse=True)
        return s[:k]