# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    if head is None:
        return SinglyLinkedListNode(data)
    tail = head
    while tail.next is not None:
        tail = tail.next
    tail.next = SinglyLinkedListNode(data)
    return head
