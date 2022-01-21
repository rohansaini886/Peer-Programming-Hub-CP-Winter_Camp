i,ii,iii = [input() for i in range(3)]
def check(a):
    try:
        c = a.index(ii)
        cc = a.index(iii,c+len(ii))
    except:
        return 0,0
    return c,cc
c = check(i)
cc = check(i[::-1])
if c[0] < c[1] and cc[0] < cc[1]: print("both")
elif c[0] < c[1]: print("forward")
elif cc[0] < cc[1]: print("backward")
else: print("fantasy")
