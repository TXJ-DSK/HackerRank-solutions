def decodeHuff(root, s):
    result = []
    curr = root
    for d in s:
        if d == '0':
            curr = curr.left
        else:
            curr = curr.right
        if curr.data != '\x00':
            result.append(curr.data)
            curr = root
    print("".join(result))
