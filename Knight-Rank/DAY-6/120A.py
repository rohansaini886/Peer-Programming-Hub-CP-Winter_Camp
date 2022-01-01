import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
print(['L','R'][(input()=='front')^(input()=='1')])
