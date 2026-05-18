class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res += st + ' '
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        workspace = ""
        for ch in s:
            if ch != ' ':
                workspace += ch
            else:
                res.append(workspace)
                workspace = ""
        return res
