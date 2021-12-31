h,m=map(int,input().split(':'))
while 1:
	m+=1
	if m==60:h+=1;m=0
	if h==24:h=0
	a=str(h);a='0'*(2-len(a))+a
	b=str(m);a+=':'+'0'*(2-len(b))+b
	if(a==a[::-1]):print(a);exit()
