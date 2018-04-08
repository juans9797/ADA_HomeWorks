from sys import stdin
#Nombre: Juan Sebastian Rivera
#Codigo de estudiante 5498445
#Codigo DFS tomado de las notas de clase del profesor Camilo Rocha

delta = [(-1,0),(0,-1),(0,1),(1,0)]
matrix,tam = None,None



def dfs(visited, row, col):
  stack = [ (row, col) ] ; visited[row][col] = 1
  while len(stack)!=0:
    r,c = stack.pop()
    for dr,dc in delta:
      if 0<=r+dr<tam and 0<=c+dc<tam and visited[r+dr][c+dc]==0:
      	if(matrix[r][c]==matrix[r+dr][c+dc] and visited[r+dr][c+dc]==0):
      		stack.append((r+dr,c+dc)) ; visited[r+dr][c+dc] = 1
    visited[r][c] = 2


def solve():
	global matrix,tam
	visited = [ [ 0 for x in range(tam) ] for y in range(tam) ]
	ans = 0
	for r in range(tam):
		for c in range(tam):
			if visited[r][c]== 0:
				ans = ans +1 
				dfs(visited,r,c)
	return ans
				



def main():
	global matrix,tam
	tam = -1
	while tam != 0:
		tam = stdin.readline().strip()
		tam = int(tam)
		if tam !=0:
			list1=[]
			matrix = [ [ tam for x in range(tam) ] for y in range(tam) ]
			for i in range(tam-1):
				line = stdin.readline().strip()
				list1=([int(x) for x in line.split() ])
				cont = 0
				while cont < len(list1)-1:
					x = list1[cont]
					y = list1[cont+1]
					matrix[int(x)-1][int(y)-1] = i+1
					cont = cont + 2
			ans = solve()
			if ans == tam:
				print("good")
			else:
				print("wrong")



main()