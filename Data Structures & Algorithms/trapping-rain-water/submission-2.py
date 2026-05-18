class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        lMax = height[l]
        rMax = height[r]
        w = 0
        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                w += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                w += rMax - height[r]
        return w