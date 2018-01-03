class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        low, high = 0, len(nums) - 1
        while low <= high:
            if low == high:
                return low
            mid = (low + high) // 2
            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid
        return mid
