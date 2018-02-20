from sys import stdin
import operator

#Juan Sebastian Rivera - 5498445
#Codigo (LIS) tomado del repositorio del profesor Camilo Rocha (https://bitbucket.org/snippets/hquilo/nrodL/lis-in-quadratic-time-with-memoization)
#Modificado segun lo discutido en la clase para la solucion del problema
#Problema discutido con Juan Sebastian Quiceno y Maria Paula Carrero

bloques = []

def cBloques(x,y,z):
	global bloques
	bloques.append([x,y,z])
	bloques.append([x,z,y])
	bloques.append([y,x,z])
	bloques.append([y,z,x])
	bloques.append([z,x,y])
	bloques.append([z,y,x])

def aux_memoization(a,n,memo):
  ans = memo[n]
  if ans==None:
    ans = 0
    for i in range(n):
      if a[i][0]>a[n][0] and a[i][1]>a[n][1] : #Modificado aqui para verificar tanto X como Y, que ambas deben ser estrictamente mayores que el siguiente
        ans = max(ans,aux_memoization(a,i,memo))
    ans += a[n][2] #Modificado aqui para no sumar 1 si no modificar el Z
    memo[n] = ans
  return ans

def lis_memoization(a):
  N = len(a)
  ans = 0
  if N!=0:
    memo = [ None for i in range(N) ]
    for n in range(N):
      ans = max(ans,aux_memoization(a,n,memo))
  return ans


def main():
	global bloques
	l = 1
	case = 1
	while int(l) != 0:
		contador = 0
		l = stdin.readline().strip()
		while contador < int(l) and int(l) != 0:
			j = stdin.readline().strip()
			x,y,z = [ int(k) for k in j.split() ]
			cBloques(x,y,z)
			contador = contador + 1
		bloques.sort(key = operator.itemgetter(0, 1),reverse=True) #Ordenar la lista aqui para enviarla al LIS, se ordena de mayor a menor primero por X y luego por Y
		if int(l) != 0:
			print("Case {}: maximum height = {}".format(case,lis_memoization(bloques)))
			case = case + 1
			bloques = []


main()


