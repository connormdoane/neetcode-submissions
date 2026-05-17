class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        swap = ''
        p1 = 0
        p2 = len(s)-1
        while p1 < p2:
            swap = s[p1]
            s[p1] = s[p2]
            s[p2] = swap
            p1 += 1
            p2 -= 1