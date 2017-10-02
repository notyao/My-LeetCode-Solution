#1 
class Solution(object):
   def findKthLargest(self, nums, k):
       """
       :type nums: List[int]
       :type k: int
       :rtype: int
       """
       return sorted(nums,reverse=True)[k-1]

#2
class Solution(object):
   def findKthLargest(self, nums, k):
       """
       :type nums: List[int]
       :type k: int
       :rtype: int
       """
       a = []
       res = 0
       for i in nums:
           heapq.heappush(a,-i)
       for j in range(k):
           res = - heapq.heappop(a)
       return res
