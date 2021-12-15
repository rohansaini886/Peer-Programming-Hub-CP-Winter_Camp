s = ''
for i in range(3):
    s += input()[0]
 
if s in ('rss', 'prr', 'spp'):
    print('F')
elif s in ('srs', 'rpr', 'psp'):
    print('M')
elif s in ('ssr', 'rrp', 'pps'):
    print('S')
else:
    print('?')
