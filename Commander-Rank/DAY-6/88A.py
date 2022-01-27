n = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'B', 'H']
i = sorted(n.index(x) for x in input().split())
c = (i[1] - i[0], i[2] - i[1])
if c in ((4, 3), (3, 5), (5, 4)):
    print('major')
elif c in ((3, 4), (4, 5), (5, 3)):
    print('minor')
else:
    print('strange')
