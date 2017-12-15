class Solution:
    def lengthOfLongestSubstring(self, s):

        dict = {}
        ans = left = 0
        for i in range(len(s)):
            if s[i] in dict and dict[s[i]] >= left:
                left = dict[s[i]] + 1
            dict[s[i]] = i
            ans = max(ans, i - left + 1)
        return ans
