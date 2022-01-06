l=lambda:map(int,input().split())
a,b=l()
for i,j in sorted(list(l()) for i in ' '*b):
	a=(a+j)*(a>i)
print('YNEOS'[a<1::2])
