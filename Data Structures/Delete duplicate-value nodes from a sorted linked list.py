# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def removeDuplicates(llist):
    curr, head = llist, llist
    while curr.next:
        if curr.next.data > curr.data:
            curr = curr.next
        else:
            curr.next = curr.next.next
    return head
