def findMergeNode(head1, head2):
    len1, len2 = 0, 0
    curr = head1
    while curr is not None:
        curr = curr.next
        len1 += 1
    curr = head2
    while curr is not None:
        curr = curr.next
        len2 += 1
    for _ in range(max(0, len1-len2)):
        head1 = head1.next
    for _ in range(max(0, len2-len1)):
        head2 = head2.next
    while head1 is not None and head2 is not None:
        if head1 == head2:
            return head1.data
        head1 = head1.next
        head2 = head2.next
