l,r=map(int,input().split())

a=[]
def foo(n):
	a.append(n)
	if n>10*r:
		return
	foo(10*n+4)
	foo(10*n+7)
	return

foo(0)
a.sort()

def get_sum(m):
	s=0
	for i in range(1,len(a)):
		s+=a[i]*(min(a[i],m)-min(a[i-1],m))
	return s

print(get_sum(r)-get_sum(l-1))

