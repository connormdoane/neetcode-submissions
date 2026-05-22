class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += ' '
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        p = 0
        while p < len(s):
            count = ''
            while s[p] != ' ':
                count += s[p]
                p += 1
            # p points to the space
            p += 1
            res.append(s[p:p+int(count)])
            p += int(count)
        return res