# 1：
for i in range(len(nums)):
   for j in range(i + 1, len(nums)):
       if nums[i] + nums[j] == target:
           return (i, j)

# 2：
class Solution(object):
   def twoSum(self, nums, target):
       """
       :type nums: List[int]
       :type target: int
       :rtype: List[int]
       """
       hash = {}
       for i in range(len(nums)):
           another_value = target - nums[i]
           if another_value in hash.keys():
               return (hash[another_value], i)
           hash[nums[i]] = i
