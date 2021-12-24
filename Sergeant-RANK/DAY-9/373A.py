from collections import Counter

I = input

k = int(I())
c = Counter(I()+I()+I()+I())

print('NO' if any(t!='.' and c[t]>2*k for t in c) else 'YES')
