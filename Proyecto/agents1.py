from sys import stdin
#Nombre: Juan Sebastian Rivera
#Codigo de estudiante: 5498445
#Codigo de Honor:
#Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
#a seguir los más altos estándares de integridad académica.

matrix,numH,conver,name = None,None,None,None

def parser():
	global matrix,numH
	for i in matrix:
		name = ""
		temp = list()
		stack = list()
		cont = 0
		for j in i:
			if j == '(':
				cont = cont + 1
				temp.append(name)
				name = ""
				stack.append(temp)
				temp = list()
			elif j == ')':
				if name != "" and len(stack) >= 2:
					var = stack.pop()
					var.append(name)
					var1 = stack.pop()
					var1.append(var)
					stack.append(var1)
					name = ""
					cont = cont - 1
				elif name != "":
					var = stack.pop()
					var.append(name)
					stack.append(var)
					name = ""
					cont = cont - 1
			elif j == ',':
				if name != "":
					var = stack.pop()
					var.append(name)
					stack.append(var)
					name = ""
			else:
				name = name+j
		print(stack)


		
def main():
	#Realiza las entradas y envia a la funcion solve
	global matrix,numH,conver,name
	line = stdin.readline().strip().split()
	while(line[0] != "END"):
		name = line[0]
		numH = int(line[1])
		matrix = list()
		conver = list()
		for _ in range(numH):
			lista = stdin.readline().strip()
			matrix.append(list(lista))
		parser()
		line = stdin.readline().strip().split()





main()
