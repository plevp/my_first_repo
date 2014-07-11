# horse
import os

board = [];
next = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
N = 0;

def doit(n, start):
	global N;
	N = n;
	l = [0] * N
	for i in range(N):
		board.append(list(l));

	board[start[0]][start[1]] = 1;
	do_move(start, 2);
	print "Failed";
	print_board();
        return "Done";

def print_board() :
    for i in range(N):
		print ' '.join('%3d' % val for val in board[i]);
		#['%3d' % val for val in board[i]];
	#print "\n"

def next_movies(cur):
	res = []
	
	for itm in next:
		nm = (cur[0] + itm[0], cur[1] + itm[1])
		if (nm[0] >=0)  and (nm[1] >=0) and (nm[1] < N) and (nm[0] < N):
			if board[nm[0]][nm[1]] == 0:
				res.append(nm)
	return res;
	
def do_move(cur, ind):
#	print "do move: ", ind, "  ", cur
#	print_board();
	nm = next_movies(cur);
	
	if len(nm) == 0:
		if ind == N * N +1:
			print "Success";
			print_board();
			os._exit(1);
		else:
			if ind == 1:
				print "Failed";
				print_board();
				os._exit(1);
			else:
				return;
	else:
		ll = [];
		for itm in nm:
			ll.append(len(next_movies(itm)));
		m = min(ll);
		
		for itm in nm:
			if (len(next_movies(itm)) == m):
				board[itm[0]][itm[1]] = ind;
				do_move(itm, ind+1);
				board[itm[0]][itm[1]] = 0;
		return;
		

#N = 5;
def foo(a,b):
	return a + b;


print "Hello"
print foo(2,3);

print doit( 8, (0,0))
print "Bye"

doit(5, (2,2));

doit (8, (0,0))
		
#print next_movies((4,5))



#board[2][2] = 1;
#do_move((2,2), 2);

#board[0][0] = 1;
#do_move((0,0), 2);
#print "Failed"
#print_board();

