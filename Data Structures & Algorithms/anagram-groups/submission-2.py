class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            characters = [0] * 26
            for ch in s:
                characters[ord(ch)-ord('a')] += 1
            res[tuple(characters)].append(s)
        return list(res.values())