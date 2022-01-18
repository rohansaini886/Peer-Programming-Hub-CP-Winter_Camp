a=m=''
for x in input()[::-1]:
    if x>=m: a+=x
    m=max(m,x)
print(a[::-1])
