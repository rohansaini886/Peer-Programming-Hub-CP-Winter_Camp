s=""
L=[]
s=input()
k=0
r=0
c=0
if s[0]=='h':
    L.append('http://')
    c=4
    s=s[c:]
elif s[0]=='f':
    L.append('ftp://')
    c=3
    s=s[c:]
r=s.find('ru',1)
L.append(s[:r])
L.append('.ru')

k=r+2

if k<len(s):
    L.append('/')
    L.append(s[k:])
   
print (''.join(L))
