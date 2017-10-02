class Solution(object):
  def strStr(self, haystack, needle):
      """
      :type haystack: str
      :type needle: str
      :rtype: int
      """
      if not needle:
          return 0
      len_h = len(haystack)
      len_n = len(needle)
      if len_n > len_h:
          return -1
      else:
          for i in range(len_h):
              if haystack[i] == needle[0]:
                  if haystack[i:i + len_n] == needle:
                      return i
      return -1
