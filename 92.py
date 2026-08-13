# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        if left == right:
            return head
        d = ListNode(0)
        d.next = head
        prev = d
        for i in range(left-1):
            prev = prev.next
        curr = prev.next
        for i in range(right-left):
            nn = curr.next
            curr.next = nn.next
            nn.next = prev.next
            prev.next = nn
        return d.next
