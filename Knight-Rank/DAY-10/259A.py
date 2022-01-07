ans="YES"
for i in range(8):
    s=input()
    if(s!=(s[0]+s[1])*4 or s[0]==s[1]):
        ans="NO"
print(ans)
