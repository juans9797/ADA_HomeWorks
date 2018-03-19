from sys import stdin

#Nombre: Juan Sebastian Rivera
#Codigo de estudiante: 5498445
#Discutido con Maria Paula Carrero


def solve(n,l,u):
	N = bin(n)[2:]
	L = bin(l)[2:]
	U = bin(u)[2:]
	maximo = max(len(N),len(L),len(U))
	N=N.zfill(32)
	L=L.zfill(32)
	U=U.zfill(32)
	N = list(N)
	L = list(L)
	U = list(U)
	m = list()
	flag1,flag2 = 1,1
	i = 32-maximo
	while i < 32 :
		if N[i] == '1':
			if L[i]=='1' and flag1 ==1:
				m.append(1)
			else:
				m.append(0)
				if U[i]=='1':
					flag2 = 0
		else:
			if U[i] == '0' and flag2 ==1:
				m.append(0)
			else:
				m.append(1)
				if L[i]=='0':
					flag1 = 0
		i = i + 1

	res = ''.join(str(e) for e in m)
	return int(res,2)		












def main():
	j,n,l,u = -1,-1,-1,-1
	while j!= '':
		j = stdin.readline().strip()
		if j != '':
			n,l,u = [ int(x) for x in j.split() ]
			print(solve(n,l,u))


main()