"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

def reverse_linkelist(self,head):
    prev =None

    while head:
        temp =head
        head =head.next
        temp.next =head
        prev =temp

    return prev 