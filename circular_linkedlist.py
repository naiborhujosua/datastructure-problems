"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
"""


def circular_linkedlist(self,head):
    slow,fast =head,head

    while fast and fast.next:
        slow=slow.next
        fast =fast.next.next

        if slow==fast:
            break
    else: 
        return None

    pointer =head

    while pointer !=fast:
        pointer = pointer.next 
        fast = fast.next

    return pointer


    