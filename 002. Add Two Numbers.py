# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        t = ans
        x = 0
        while l1 or l2:
            x = x // 10
            if l1:
                x += l1.val
                l1 = l1.next
            if l2:
                x += l2.val
                l2 = l2.next

            ans.val = x % 10
            if l1 or l2:
                ans.next = ListNode(0)
                ans = ans.next
            else:
                if x > 9:
                    ans.next = ListNode(1)
        return t
