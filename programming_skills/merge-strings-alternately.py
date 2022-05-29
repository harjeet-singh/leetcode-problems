def mergeAlternately(word1: str, word2: str) -> str:
    merged = ''
    n1 = len(word1)
    n2 = len(word2)
    n = n1 if n1 < n2 else n2
    for i in range(n):
        merged += word1[i]
        merged += word2[i]

    if n1 < n2:
        merged += word2[n1:]
    else:
        merged += word1[n2:]

    return merged

# def mergeAlternately(w1, w2):
#        return ''.join(a + b for a, b in zip_longest(w1, w2, fillvalue=''))
