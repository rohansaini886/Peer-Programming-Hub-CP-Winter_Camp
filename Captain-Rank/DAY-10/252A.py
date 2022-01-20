n = int(input())
arr = list(map(int, input().split()))
best = 0
for i in range(n):
	x = 0
	for j in range(i, n):
		x = (x^arr[j])
		best = max(best, x)
print(best)
