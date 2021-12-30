s=input()
c=0
while len(s)>1:
	s=str(sum(map(int,s)))
	c+=1
print(c)
