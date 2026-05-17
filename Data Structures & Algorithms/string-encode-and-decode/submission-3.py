class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # Start of length value
        while i < len(s):
            j = i+1 # End of length value / '#'
            while s[j] != "#": 
                j += 1
            length = int(s[i:j]) # Store the length of this substring
            res.append(s[j+1: j+1+length]) # Append the corresponding number of chars as a string
            i += length + 1 + len(str(length)) # Increment i based on length, '#', and the length of the encoded substring length value
        return res
