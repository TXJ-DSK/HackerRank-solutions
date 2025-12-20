def has_cycle(head):
    if head is None:
        return 1
    slow, fast = head, head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return 1
    return 0
