"""Given the head of a singly linked list, return the middle node of the linked list."""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fastMover, slowMover = head, head
        while(fastMover and fastMover.next):
            slowMover = slowMover.next
            fastMover = fastMover.next.next
        return slowMover