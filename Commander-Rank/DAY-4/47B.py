r = dict(A = [], B = [], C = [])
for i in range(3):
    s = input()
    if s[1] == '>':
        r[s[0]].append(s[2])
    else:
        r[s[2]].append(s[0])
l = dict()
for i in r.items():
    l[len(i[1])] = i[0]
if len(l) != 3:
    print ('Impossible')
else:
    for i in range(3):
        print(l[i],end='')
