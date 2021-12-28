n = int(input())
s = set()
for i in range(n):
	x, d = [int(x) for x in input().split()]
	if (x + d, -d) in s:
		print('YES')
		exit()
	s.add((x, d))
print('NO')
