class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di = {}
        output = []
        for i in nums:
            if i in di:
                di[i] += 1
            else:
                di[i] = 1
        for j in range(k):
            m = max(di, key=di.get)
            output.append(m)
            del di[m]
        return output