s = ['S', 'M', 'L', 'XL', 'XXL']
t = list(map(int, input().split()))
def g(si):
    if si < 0 or si >= 5 or not t[si]:
        return False
    else:
        print(s[si])
        t[si] -= 1
        return True
def f(si):
    for j in range(5):
        if g(si + j) or g(si - j):
            return
for i in range(int(input())):
    f(s.index(input()))
