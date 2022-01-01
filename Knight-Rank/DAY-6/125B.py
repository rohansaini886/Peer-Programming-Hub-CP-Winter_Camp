s=input()
s1=s.split('<')
del s1[0]
c=0
for i in s1:
	if '/' in i:
		print('  '*(c-1),'<',i,sep='')
		c-=1
	else:
		print('  '*c,'<',i,sep='')
		c+=1
