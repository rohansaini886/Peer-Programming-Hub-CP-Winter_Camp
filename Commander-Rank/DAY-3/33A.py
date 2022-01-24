n, m, k = map(int, input().split())
d = [-1 for i in range(m)]
 
for i in range(n):
    r, c = map(int, input().split())
    r -= 1
    d[r] = c if d[r] == -1 else min(d[r], c)
 
ans = 0
for i in d:
    ans += i
 
print(min(ans, k))
