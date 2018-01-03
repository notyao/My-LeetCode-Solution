class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = 0
        right = len(letters)
        middle = int((left + right) / 2)
        while left < right:
            if letters[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
            middle = int((left + right) / 2)
        print(middle)
        if middle == len(letters) - 1 or middle == len(letters) or middle == -1:
            return letters[0]
        elif letters[middle] <= target:
            return letters[middle + 1]
        else:
            return letters[middle]
