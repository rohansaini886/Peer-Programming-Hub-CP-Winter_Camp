n=int(input())
count=0
s="ABSINTH,BEER,BRANDY,CHAMPAGNE,GIN,RUM,SAKE,TEQUILA,VODKA,WHISKEY,WINE"
d=s.split(',')
for i in range(n):
	s=input()
	try:
		x=int(s)
		if x<18:
			count+=1
	except:
		if s in d:
			count+=1
print(count)
