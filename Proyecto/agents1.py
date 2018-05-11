from sys import stdin
#Nombre: Juan Sebastian Rivera
#Codigo de estudiante: 5498445
#Codigo de Honor:
#Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
#a seguir los más altos estándares de integridad académica.

matrix,numH,conver,name = None,None,None,None

def parser(i):
	name = ""
	temp = list()
	stack = list()
	for j in i:
		if j == '(':
			if len(stack)==0:
				temp.append(name)
				stack.append(temp)
				stack.append([])
				name = ""
				temp = list()
			elif len(stack) >= 1:
				var = stack.pop()
				var.append(name)
				stack.append(var)
				stack.append([])
				name = ""
		elif j == ')':
			if name != "":
				var = stack.pop()
				var.append(name)
				var1 = stack.pop()
				var1.append(var)
				stack.append(var1)
				name = ""
			elif name == "":
				var = stack.pop()
				var1 = stack.pop()
				var1.append(var)
				stack.append(var1)
		elif j == ',':
			if len(stack) == 0 and name != "":
				temp.append(name)
				stack.append(temp)
				name = ""
				temp = list()
			elif len(stack)>=1 and name != "":
				var = stack.pop()
				var.append(name)
				stack.append(var)
				name = ""
		else:
			name = name + j
	while len(stack)>=2:
		var = stack.pop()
		var1 = stack.pop()
		var1.append(var)
		stack.append(var1)
	if name != "":
		var = stack.pop()
		var.append(name)
		name = ""
		stack.append(var)

	return stack.pop()


def solve():
	global matrix
	l = len(matrix)
	for i in range(l-1):
		var1 = parser(matrix[i])
		var2 = parser(matrix[i+1])
		print(var1,var2)
		solve2(var1,var2)


def solve2(var1,var2):
	l = len(var1)
	for i in range(l-1):
		if isVariable(var1[i]):
			print("Variable")
			#print(var1[i])
		elif not isVariable(var1[i]) and isinstance(var1[i+1],list):
			print("Funcion")


def isVariable(a):
	#Verifica si la variable a que ingreso, esta dentro del ASCII de las
	#Mayusculas
	a = list(a)
	if(ord(a[0])>=65 and ord(a[0])<= 90):
		return True
	else:
		return False




		
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
		solve()
		line = stdin.readline().strip().split()





main()
