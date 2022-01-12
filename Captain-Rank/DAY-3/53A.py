a=input()
b=int(input())
c=[]
for i in range(b):
	d=input()
	if d[:len(a)]==a:
		c.append(d)
if len(c)>0:
	print(min(c))
else:
	print(a)
