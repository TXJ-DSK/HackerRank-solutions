# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def sortedInsert(llist, data):
    dummy_head = DoublyLinkedListNode(0)
    dummy_head.next = llist
    curr = dummy_head
    while curr.next:
        if data <= curr.next.data:
            next_node = curr.next
            new_node = DoublyLinkedListNode(data)
            curr.next = new_node
            new_node.next = next_node
            new_node.prev = curr
            if next_node:
                next_node.prev = next_node
            return dummy_head.next
        curr = curr.next
    curr.next = DoublyLinkedListNode(data)
    curr.next.prev = curr
    return dummy_head.next
