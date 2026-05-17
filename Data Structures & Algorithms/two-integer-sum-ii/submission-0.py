class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = 1
        while numbers[p1] + numbers[p2] != target:
            if p2 == len(numbers)-1:
                p1 += 1
                p2 = p1 + 1
                continue
            p2 += 1
        return [p1+1, p2+1]
            
