# Recrusive solution, stack demanding
def reversePrint(llist):
    if llist is None:
        return
    reversePrint(llist.next)
    print(llist.data)

# Iterative solution, space demanding
def reversePrint(llist):
    if llist is None:
        return
    nums = []
    while llist is not None:
        nums.append(llist.data)
        llist = llist.next
    for i in range(len(nums)-1, -1, -1):
        print(nums[i])
