from sys import stdin
import math

#Nombre: Juan Sebastian Rivera
#Codigo de estudiante: 5498445
#Discutido con Juan Fernando Escobar, Juan Sebastian Quiceno
#Codigo mic tomado y modificado del repositorio del profesor Camilo Rocha.
def calcrad(a,b):
	ans = math.sqrt((a*a)-(b*b))
	return ans


def mic(a):
  a.sort(key=lambda x: x[1])
  n,N = 0,len(a)
  cont = 1
  while n!=N:
    best,n = n,n+1
    while n!=N :
      if a[n][0]>a[best][1]:
      	cont = cont +1
      	best = n
      n += 1
  return cont


def main():
	l,g = -1, -1
	case = 1
	while l!= 0 and g != 0:
		n = stdin.readline().strip()
		l,g = [ int(x) for x in n.split() ]
		if l!=0 and g!=0:
			cont = 0
			a = list()
			flag = 0
			while cont != l:
				n = stdin.readline().strip()
				xi,ri = [ int(x) for x in n.split() ]
				if ri > g:
					flag = 1
				if flag == 0:
					calc = calcrad(g,ri)
					left = xi-calc
					right = xi+calc
					a.append([left,right,cont])
				cont = cont + 1
			if flag == 0:		
				print("Case {}: {}".format(case,mic(a)))
			else:
				print("Case {}: {}".format(case,-1))
			n = stdin.readline().strip()
			case = case + 1




main()



