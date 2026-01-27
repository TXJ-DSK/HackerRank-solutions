# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reverse(llist):
    curr_node = llist
    next_node = curr_node.next
    curr_node.next = None
    while next_node is not None:
        next_next_node = next_node.next
        next_node.next = curr_node
        curr_node = next_node
        next_node = next_next_node
    return curr_node
