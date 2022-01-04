r1,r2=map(int,input().split())
c1,c2=map(int,input().split())
d1,d2=map(int,input().split())
a=(d1+c1-r2)//2
b=r1-a
c=c1-a
d=d1-a
if 1<=a<=9 and 1<=b<=9 and 1<=c<=9 and 1<=d<=9 and len(set([a,b,c,d]))==4:
	print(a,b)
	print(c,d)
else:
	print(-1)
