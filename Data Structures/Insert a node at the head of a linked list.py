def insertNodeAtHead(llist, data):
    newHead = SinglyLinkedListNode(data)
    newHead.next = llist
    return newHead
