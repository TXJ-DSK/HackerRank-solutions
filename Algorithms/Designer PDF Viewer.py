def designerPdfViewer(h, word):
    max_height = 0
    for c in word:
        max_height = max(max_height, h[ord(c) - ord('a')])
    return max_height * len(word)
