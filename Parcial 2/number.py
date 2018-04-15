from sys import stdin
from heapq import heappop,heappush
delta = [(-1,0),(0,-1),(0,1),(1,0)]
INF = float('inf')
m1,n1 = None,None
#Nombre: Juan Sebastian Rivera
#Codigo de estudiante 5498445
#Codigo sssp del profesor Camilo Rocha
#Trabajado con Maria Paula Carrero, Juan Sebastian Quiceno
def sssp(G,source,a):
  global m1
  dist = [ INF for _ in range(n1*m1) ]
  visited = [ False for _ in range(n1*m1) ]
  heap = [ (a,source) ]
  while len(heap)!=0:
    d,u = heappop(heap)
    if not(visited[u]):
      visited[u] = True
      for v,w in G[u]:
        if dist[v]>d+w:
          dist[v] = d+w
          heappush(heap,(dist[v],v))
  return dist







def main():
	global n1,m1,delta
	line = stdin.readline().strip()
	for _ in range(int(line)):
		n = stdin.readline().strip()
		m = stdin.readline().strip()
		n1 = int(n)
		m1 = int(m)
		matrix = list()
		dist=list()
		lista = [[] for _ in range(m1*n1)]
		for _ in range(n1):
			matrix.append([])
		for i in range(n1):
			fila =[ int(x) for x in stdin.readline().split() ]
			matrix[i]=fila
		k = 0
		for i in range(n1):
			for j in range(m1):
				lista[k].append([k,matrix[i][j]])
				for dr,dl in delta:
					if i+dr >= 0 and i+dr<n1 and j+dl>=0 and j+dl <m1:
						if i+dr > i or i+dr < i:
							lista[k].append([k+(dr*m1),matrix[i+dr][j]])
						elif j+dl < j or j+dl > j:
							lista[k].append([k+dl,matrix[i][j+dl]])
				k = k + 1
		ans = sssp(lista,0,matrix[0][0])
		print(ans[n1*m1-1])




main()