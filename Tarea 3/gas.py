from sys import stdin

#Nombre: Juan Sebastian Rivera
#Codigo de estudiante: 5498445
#Codigo mic_wf tomado de la pagina del profesor Camilo Rocha, como se discutio en clase con pequeñas modificaciones https://bitbucket.org/snippets/hquilo/z6KbA


def mic_wf(L,H,a):
  a.sort()
  ans,low,n,ok,N = list(),L,0,True,len(a)
  while ok and low<H and n!=N:
    ok = a[n][0]<=low
    best,n = n,n+1
    while ok and n!=N and a[n][0]<=low:
      if a[n][1]>a[best][1]:
        best = n
      n += 1
    ans.append(best)
    low = a[best][1]
  ok = ok and low>=H
  if ok==False:
    ans = list()
  return len(ans) #Se retorna la cantidad de estaciones que se utilizan, si es 0 es porque algun segmento del camino no se cubre




def main():
	l,g = -1,-1
	while l!=0 and g!=0:
		n = stdin.readline().strip()
		l,g = [ int(x) for x in n.split() ]
		if l!=0 and g!=0:
			cont = 0
			a = list()
			while cont != g:
				n = stdin.readline().strip()
				xi,ri = [ int(x) for x in n.split() ]
				a.append([xi-ri,xi+ri])
				cont = cont + 1
			ans= mic_wf(0,l,a)
			if ans == 0:   #Se evalua si es 0 es porque un segmento no se cubre y se retorna -1
				print(-1)
			else: #De lo contrario, la cantidad de estaciones a eliminar, es la cantidad total de estaciones menos las que necesito.
				print(g-ans)


main()