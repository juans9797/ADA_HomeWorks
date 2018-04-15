from sys import stdin
from heapq import heappop,heappush
INF = float('inf')
#Nombre: Juan Sebastian Rivera
#Codigo de estudiante: 5498445
#Trabajado con Maria Paula Carrero
#Codigo SSSP de la pagina del profesor camilo rocha

def sssp(G,source,n):
	dist = [ INF for i in range(int(n)) ]
	dist[source] = 0
	visited = [ False for i in range(len(G)) ]
	heap = [ (0,source) ]
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
	cases = stdin.readline().strip()
	case = int(cases)
	while case:
		blank = stdin.readline().strip()
		n = stdin.readline().strip()
		e = stdin.readline().strip()
		t = stdin.readline().strip()
		m = stdin.readline().strip()
		vector = list()
		suma = 0
		for _ in range(int(n)):
			vector.append([])
		for _ in range(int(m)):
			u,v,w = stdin.readline().strip().split()
			vector[int(v)-1].append([int(u)-1,int(w)])

		ans = sssp(vector,int(e)-1,int(n))
		case = case - 1
		for i in range(int(n)):
			if ans[i] <= int(t):
				suma = suma + 1
		print(suma)
		print()



main()