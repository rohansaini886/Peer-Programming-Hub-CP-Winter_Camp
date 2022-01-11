from collections import Counter
s1=input()
d=Counter(s1)
s2=input()
s2=s2.replace(' ','')
flag='YES'
for i in s2:
    if d[i]<=0:
        flag='NO'
        break
    else:
        d[i]-=1
print(flag)
