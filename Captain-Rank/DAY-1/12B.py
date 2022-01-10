s=input()
k=s.count('0')
s=''.join(sorted(s))[k:]
print(['WRONG_ANSWER','OK'][input()==('0' if s=='' else s[0]+'0'*k+s[1:])])
