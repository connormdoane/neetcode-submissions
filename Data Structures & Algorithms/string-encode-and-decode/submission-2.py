class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res += st + '\u03A9'
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        workspace = ""
        for ch in s:
            if ch != '\u03A9':
                workspace += ch
            else:
                res.append(workspace)
                workspace = ""
        return res
