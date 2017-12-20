class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        neww = nums1[:m] + nums2[:n]
        neww.sort()
        for i in range(len(nums1)):
            if len(neww) == i:
                break
            nums1[i] = neww[i]
