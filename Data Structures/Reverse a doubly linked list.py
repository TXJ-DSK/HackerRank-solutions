# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def reverse(llist):
    if not llist or not llist.next:
        return llist
    prev_node = None
    next_node = llist.next
    while llist:
        llist.next = prev_node
        llist.prev = next_node
        if next_node:
            next_node = next_node.next
        prev_node = llist
        llist = llist.prev
    return prev_node
