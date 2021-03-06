# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        previous = None
        while head:
            current = head
            head = head.next
            current.next = previous
            previous = current
        return previous
