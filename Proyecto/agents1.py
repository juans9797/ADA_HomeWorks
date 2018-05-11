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
	if name != "" and len(stack)>=1:
		var = stack.pop()
		var.append(name)
		name = ""
		stack.append(var)
	elif name != "" and len(stack)==0:
		temp.append(name)
		stack.append(temp)
		name = ""
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
	l = min(len(var1),len(var2))
	print(l)
	for i in range(l-1):
		#-------------AQUI TOCA REVISAR EL RANGO-------------------#
		print(i)
		if isVariable(var1[i]):
			print("--Entro")
			if not isVariable(var2[i]) and isinstance(var2[i+1],list):
				var3 = var1[i]
				print("Entro")
				for j in var2[i+1]:
					if isinstance(j,list):
						if var3 == j:
							print("Se exploto")
							return False
						else:
							return True
					else:
						if var3 == j:
							return False
						else:
							return True


		elif not isVariable(var1[i]) and isinstance(var1[i+1],list):
			if not isVariable(var2[i]) and isinstance(var2[i+1],list):
				if var1[i] != var2[i]:
					return False
				else:
					print("Aqui toca hacer algo")
			else:
				return False
		elif not isVariable(var1[i]) and not isinstance(var1[i+1],list):
			if var1[i]==var2[i]:
				print("Si")
			else:
				return False
		else:
			return True

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