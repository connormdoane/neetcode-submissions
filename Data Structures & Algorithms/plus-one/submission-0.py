class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True # Begin at true to represent initial plus one
        i = len(digits)-1
        while carry and i > -1:
            digits[i] += 1
            digits[i] %= 10
            if digits[i] != 0:
                carry = False
            i -= 1
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits