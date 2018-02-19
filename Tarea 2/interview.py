from sys import stdin
memo=[[0 for x in range(0,61)]for y in range(0,61)]
def solve(n,back):
	global memo
	if n<=1:
		return 1
	else:
		if memo[n][back]!=0:
			return memo [n][back]
		else:
			memo[n][back]= 1
			for i in range(1,back+1):
				memo[n][back]= memo[n][back]+solve(n-i,back)
			return memo[n][back]



def main():
	n,k,contador = 0,0,1
	while(n<=60):
			l = stdin.readline().strip()
			n,k = [ int(x) for x in l.split() ]
			if(n<=60):
				print("Case {}: {}".format(contador,solve(n,k)))
				contador = contador + 1

main()