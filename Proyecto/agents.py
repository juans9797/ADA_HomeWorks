from sys import stdin
#Nombre: Juan Sebastian Rivera
#Codigo de estudiante: 5498445
matrix, numH = None,None

def isVariable(a):


def solve():
	global matrix,numH
	for i in range(numH):
		for j in range(i+1,numH):
			pass
			



def main():
	global matrix,numH
	line = stdin.readline().strip().split()
	while(line[0] != "END"):
		name = line[0]
		numH = int(line[1])
		matrix = list()
		for _ in range(numH):
			lista = stdin.readline().strip()
			matrix.append(list(lista))
		solve()
		line = stdin.readline().strip().split()





main()
