a = input()
s = sorted(input())

print(''.join(s.pop() if s and s[-1] > d else d for d in a))
	  			 				 	     			    		  	
