class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):
            a = (digits[i] + 1) // 10
            digits[i] = (digits[i] + 1) % 10
            if a == 0: return digits
        if a == 1:
            digits.insert(0, 1)
        return digits
