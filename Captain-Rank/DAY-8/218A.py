n, k = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(1, len(arr), 2):
    if (k > 0 and arr[i] - 1 > max(arr[i-1], arr[i+1])):
        arr[i] -= 1
        k -= 1
print(*arr)
