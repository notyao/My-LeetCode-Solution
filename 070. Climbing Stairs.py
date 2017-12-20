class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = {1: 1, 2: 2}
        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]
        return ways[n]