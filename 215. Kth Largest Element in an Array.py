# def  # # Find the kth largest element in an unsorted array.


# Note that it is the kth largest element in the sorted order,
# not the kth distinct element.

# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5. 
# [1, 2, 3, 4, 5, 6]


# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.

# step1: sort array
# step2: ascending
# step3: return last k element 

def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    newnums = sorted(nums)
    return newsnums[len(newnums) - 1]
