# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(llist, data, position):
    if position == 0:
        new_node = SinglyLinkedListNode(data, llist)
        return new_node
    count = 1
    prev_node = llist
    while count < position:
        prev_node = prev_node.next
        count += 1
    new_node = SinglyLinkedListNode(data)
    new_node.next = prev_node.next
    prev_node.next = new_node
    return llist
