def MeargeSort(l, r):
    if r - l == 1:
        return [a[l]]
    m = (l + r) // 2
    L = MeargeSort(l, m)
    R = MeargeSort(m, r)
    res = []
    i = j = 0
    while i < len(L) or j < len(R):
        if i == len(L):
            res.append(R[j])
            j += 1
        elif j == len(R):
            res.append(L[i])
            i += 1
        elif L[i] <= R[j]:
            res.append(L[i])
            i += 1
        else:
            res.append(R[j])
            j += 1
    return res


n = int(input())
a = list(map(int, input().split()))
print(*MeargeSort(0, n))
