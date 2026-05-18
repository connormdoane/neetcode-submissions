class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        ways = [1, 1]
        for i in range(1, n):
            ways.append(ways[i-2] + ways[i-1] + 1)
        return ways[-1]
