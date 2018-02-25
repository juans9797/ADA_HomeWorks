from sys import stdin
tab=[[0 for x in range(0,301)]for y in range(0,301)]
tab[0][0]=1

#Juan Sebastian Rivera - 5498445
#Discutido con Juan Sebastian Quiceno y Maria Paula Carrero
#Basado en la solucion planteada en clase del prof Camilo Rocha (ADA)
#Codigo tomado de los apuntes de Maria Paula Carrero

def crearTab():
	m,n,l = 1,0,1
	while(m !=301):
		if(l == 301):
			m,n,l=m+1,0,1
		elif(n== 301):
			n,l=0,l+1
		else:
			if(m<=n):
				tab[l][n] = tab[l][n]+tab[l-1][n-m]
			n = n + 1


def main():
	l = '1'
	while(l!=''):
		l = stdin.readline().strip()
		n = [ int(x) for x in l.split() ]
		if(len(n) >=1):
			ans = 0
			if(len(n)==1):
				for w in range(0,int(n[0]+1)):
					ans = ans + tab[w][n[0]]
			elif(len(n)==2):
				for w in range(0,min(int(n[0])+1,int(n[1]+1))):
					ans = ans + tab[w][n[0]]
			elif(len(n)==3):
				for w in range(int(n[1]),min(int(n[0])+1,int(n[2])+1)):
					ans = ans + tab[w][n[0]]
			print(ans)

crearTab()
main()