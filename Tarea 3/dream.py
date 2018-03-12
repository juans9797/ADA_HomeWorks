from sys import stdin

#Nombre: Juan Sebastian Rivera
#Codigo de estudiante: 5498445
#Discutido con Juan Fernando Escobar, Carlos Arboleda

def solve(a):
	cont = 0
	tot = 0
	flag = 0
	while cont < len(a):
		if a[cont]=='?':
			a[cont] = '0'
		if a[cont]=='1':
			if flag == 0:
				flag = flag + 3
			else:
				flag = flag + 1
		elif a[cont]=='0':
			if flag == 0:
				tot = tot + 1
			else:
				flag = flag -1
		if flag == 1:
			flag=0
			tot = tot + 1
		cont = cont+1
	if flag == 0:
		return tot
	else:
		return 0




def main():
	n = '1'
	while n!= '':
		n = stdin.readline().strip()
		if n!='':
			l = list(n)
			ans = solve(l)
			print(ans)
			


main()