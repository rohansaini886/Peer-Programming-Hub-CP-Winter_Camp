x, y, a, b = map(int, input().split())
ans = []
 
for i in range(a, x + 1):
	for j in range(b, y + 1):
		if i > j:
			ans.append((i, j))
 
print(len(ans))
[print(x[0], x[1]) for x in ans]
