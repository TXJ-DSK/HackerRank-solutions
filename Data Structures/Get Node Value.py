def getNode(llist, positionFromTail):
    curr, tail = llist, llist
    for _ in range(positionFromTail):
        tail = tail.next
    while tail.next is not None:
        curr = curr.next
        tail = tail.next
    return curr.data
