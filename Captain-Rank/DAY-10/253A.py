ip = open("input.txt","r")
op = open('output.txt','w')
n,m = map(int,ip.readline().split())
if n>=m:
	res = 'BG'*m+'B'*(n-m)
else:
	res = 'GB'*n+'G'*(m-n)	
op.write(res)
