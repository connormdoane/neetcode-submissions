class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        ways = [1, 2]
        for i in range(2, n):
            ways.append(ways[i-1] + ways[i-2])
        return ways[-1]