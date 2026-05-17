class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers)-1
        while numbers[p1] + numbers[p2] != target:
            value = numbers[p1] + numbers[p2]
            if value > target:
                p2 -= 1
                continue
            if value < target:
                p1 += 1
                continue
        return [p1+1, p2+1]
            
            
