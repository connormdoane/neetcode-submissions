class Solution:
    def trap(self, height: List[int]) -> int:
        pre = [0] * len(height)
        suf = [0] * len(height)
        w = 0
        pre[0] = height[0]
        suf[-1] = height[-1]
        for i in range(1, len(height)):
            pre[i] = max(pre[i-1], height[i])
        for i in range(len(height)-2, -1, -1):
            suf[i] = max(suf[i+1], height[i])
        for c in range(len(height)):
            w += min(pre[c], suf[c]) - height[c]
        return w