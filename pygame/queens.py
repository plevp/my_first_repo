import main_queen

import random;
	
def foo(n):
	v = list(range(n));
#	print v;
	for index in range(n-1, -1, -1):
#		print index;
		s = random.randint(0,10000);
		random.seed(s);
		t0 = random.randint(0,index)
		t = v[t0]
		t1 = v[index]
#		print "index: ", index, " t0: ", t0, " t: ", t, " t1: ", t1
		v[index] = t;
		v[t0] = t1 
#		print v;
	return v;

def check(li, k): 

	if (k > 0):
		for i in range(k):
			if (li[i] == li[k]):
				return False;
			else:
				if abs(li[i] - li[k]) == (k-i):
					return False;
	return True;
	
def f1(n):
	done = False;
	li = n * [0];
	j = 0; # index
	
	while (done == False):
		# set value
		if check(li, j) == True:  # good 
			if n == (j +1): # finish
				print "Succeed";
				# print li;
				done = True;
			else: # do next
				j = j + 1;
				li[j] = 0;
		else: # failed, try next position
			while ( j >= 0):  
				if  li[j] < n:
					li[j] = li[j]+1;
					break;
				else:
					j = j - 1;
			if j < 0:
				print "Failed";
				print li;
				done = True;	
			 
	return li
				

#print "Hello";
#print foo(7);

print f1(5);

l8 = f1(8)

main_queen.draw_board(l8)








