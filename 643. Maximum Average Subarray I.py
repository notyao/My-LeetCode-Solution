class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maximum = temp = sum(nums[:k])
        for i in range(1, len(nums) - k + 1):
            temp = temp - nums[i - 1] + nums[i + k - 1]
            maximum = max(temp, maximum)
        return maximum / k
