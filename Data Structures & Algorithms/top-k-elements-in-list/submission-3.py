class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums: # Populate dictionary
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items(): # Convert into frequency buckets
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1): # Loop backwards through buckets to find K most
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
