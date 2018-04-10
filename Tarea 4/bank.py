from sys import stdin
from heapq import heappop,heappush

#Nombre: Juan Sebastian Rivera
#Codigo de estudiante: 5498445
#Trabajado con: Carlos Arboleda, Maria P Carrero
#Codigo sssp tomado de la pagina del prof. Camilo Rocha (ADA 20181)

INF = float('inf')

def sssp(G,source):
  dist = [ INF for i in range(len(G)) ]
  visited = [ False for i in range(len(G)) ]
  heap = []
  for i in range(len(source)):
  	dist[source[i]]= 0
  	heappush(heap,(0,source[i]))
  while len(heap)!=0:
    d,u = heappop(heap)
    if not(visited[u]):
      visited[u] = True
      for v,w in G[u]:
        dist[v] = min(dist[v],w+dist[u])
        if visited[v]==False:
          heappush(heap,(dist[v],v))
  return dist


def main():
	line = -1
	while line != "":
		line = stdin.readline().strip()
		if line != "":
			n,m,b,p=([int(x) for x in line.split() ])
			grafo = [list() for _ in range(n)]
			for _ in range(m):
				line = stdin.readline().strip()
				u,v,t=([int(x) for x in line.split() ])
				grafo[u].append([v,t])
				grafo[v].append([u,t])
			banks = [0 for _ in range(len(grafo))]
			bankslist = stdin.readline().strip().split()
			for i in bankslist:
				banks[int(i)]=1
			police = list()
			if p != 0:
				policelist = stdin.readline().strip().split()
				for i in policelist:
					police.append(int(i))
			#print(police)

			distancia = sssp(grafo,police)
			#print(distancia)
			var1 = 0
			var2 = 0
			for i in range(n):
				if banks[i]==1:
					var1 = max(var1,distancia[i])
			for i in range(n):
				if var1 == distancia[i] and banks[i]==1:
					var2 = var2 + 1
			if var1 == INF:
				print(var2,'*')
			else:
				print(var2,var1)
			for i in range(n):
				if var1 == distancia[i] and banks[i]==1:
					var2 = var2 -1
					if var2 != 0:
						print(i,"",end="")
					else:
						print(i)






main()