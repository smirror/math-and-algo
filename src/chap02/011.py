n = int(input())
ans = [i for i in range(2, n + 1)]
for i in range(2, n + 1):
    for j in range(i*2, n + 1, i):
        if j in ans:
            ans.remove(j)
print(*ans)
