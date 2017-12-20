class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0

        if x < 0:
            res = int(str(x * -1)[::-1]) * -1
        if x > 0:
            res = int(str(x)[::-1])
        if abs(res) > 2147483647:
            return 0
        else:
            return res
