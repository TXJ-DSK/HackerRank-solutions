# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    dummy = SinglyLinkedListNode(0)
    curr = dummy
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            curr.next = head1
            head1 = head1.next
            curr = curr.next
            curr.next = None
        else:
            curr.next = head2
            head2 = head2.next
            curr = curr.next
            curr.next = None
    if head1 is None and head2 is not None:
        curr.next = head2
    elif head2 is None and head1 is not None:
        curr.next = head1
    return dummy.next
