class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        i = len(a) - 1
        j = len(b) - 1
        jinwei = 0
        while i >= 0 or j >= 0:
            m = n = 0
            if i >= 0:
                m = int(a[i])
                i -= 1
            if j >= 0:
                n = int(b[j])
                j -= 1
            c = m + n + jinwei
            if c == 3:
                jinwei = 1
                r = "1"
            elif c == 2:
                jinwei = 1
                r = "0"
            elif c == 1:
                jinwei = 0
                r = "1"
            else:
                jinwei = 0
                r = "0"
            result = r + result
        if jinwei == 1:
            result = "1" + result
        return result
