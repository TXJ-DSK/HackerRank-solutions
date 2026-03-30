def compare_lists(llist1, llist2):
    while True:
        if llist1 is None and llist2 is None:
            return 1
        elif llist1 is None or llist2 is None:
            return 0
        elif llist1.data != llist2.data:
            return 0
        llist1 = llist1.next
        llist2 = llist2.next
