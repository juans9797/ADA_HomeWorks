from sys import stdin

#Nombre: Juan Sebastian Rivera
#Codigo de estudiante: 5498845

def verificar(l):
	it = 0
	ans = True
	while it < len(l) and ans == True:
		if l[it]!=l[len(l)-it-1]:
			ans = False
		it = it + 1
	return ans



def solve(l):
	tab = [101 for i in range(len(l)+1)]
	tab[0]=0
	cont = 0
	while cont <= len(l):
		for j in range(cont):
			ans = verificar(l[j:cont])
			if ans == True:
				tab[cont] = min(tab[cont],1+tab[j])
		cont = cont + 1
	return tab[len(l)]




def main():
	l='1'
	while(l!=''):
		l = stdin.readline().strip()
		n = list(l)
		if(l!=''):
			print(solve(n))	


main()