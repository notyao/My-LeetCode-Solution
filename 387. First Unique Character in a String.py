class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        for i in s:
            if i in dict.keys():
                dict[i] += 1
            else:
                dict[i] = 1

        for i in range(len(s)):
            c = s[i]
            if dict[c] == 1:
                return i
        return -1
