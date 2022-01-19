A, B, ans = 1000000000, 1, -1
for i in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    if a < A:
        A = a
        ans = -1
    if b > B:
        B = b
        ans = -1
    if a == A and b == B: ans = i
print(ans)
