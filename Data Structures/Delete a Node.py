def deleteNode(llist, position):
    dummy = SinglyLinkedListNode(-999)
    dummy.next = llist
    curr = dummy
    for _ in range(position):
        curr = curr.next
    curr.next = curr.next.next
    return dummy.next
