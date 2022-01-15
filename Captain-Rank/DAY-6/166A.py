n,k = map(int,input().split())
s = []

for i in range(n):
	a,b = map(int,input().split())
	r = a**a-b
	s.append(r)


s.sort(reverse=True)


print(s.count(s[k-1]))
