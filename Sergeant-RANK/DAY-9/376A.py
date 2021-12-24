a=input()
p=a.index('^')
c=sum((i-p)*int(y) for i,y in enumerate(a) if y.isdigit())
print([['balance','right'][c>0],'left'][c<0])
