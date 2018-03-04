from sys import stdin

#Nombre: Juan Sebastian Rivera
#Codigo de estudiante: 5498445

def solve(n,m,v):
	low = v[0]
	hi = 0
	mid = 0
	for i in v:
		hi = hi + i

	while low <= hi:
		cont = 0
		acc = 0
		acc2 = 0
		mid = low+((hi-low)//2)
		while cont < n:
			if (mid < max(v)):
				acc2 = m + 1
				cont = n
			elif acc + v[cont] > mid:
				acc2 = acc2 + 1
				acc = v[cont]
			else:
				acc = acc + v[cont]
			cont = cont + 1

		if acc2 < m:
			hi = mid-1
		else:
			low = mid+1

	return hi+1




def main():
	l = '1'
	while(l!= ''):
		l = stdin.readline().strip()
		if(l != ''):
			n,m = [ int(x) for x in l.split() ]
			l = stdin.readline().strip()
			v = [ int(x) for x in l.split() ]
			print(solve(n,m,v))




main()