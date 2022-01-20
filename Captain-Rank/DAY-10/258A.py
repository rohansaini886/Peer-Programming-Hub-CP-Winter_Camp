n=input()
z=max(0,n.find('0'))
print(n[:z]+n[z+1:])
