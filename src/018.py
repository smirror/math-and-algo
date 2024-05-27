from collections import Counter

n = int(input())
a = list(map(int, input().split()))

cnt = Counter(a)
print(cnt[100] * cnt[400] + cnt[200] * cnt[300])
