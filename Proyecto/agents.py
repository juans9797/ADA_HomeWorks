from sys import stdin
#Nombre: Juan Sebastian Rivera
#Codigo de estudiante: 5498445
matrix, numH, conver, already, name = None,None,None,None,None

def isVariable(a):
	if(ord(a)>=65 and ord(a)<= 90):
		return True
	else:
		return False

def isLowerCase(a):
	if(ord(a)>=97 and ord(a)<=122):
		return True
	else:
		return False

def makeString(a):
	cont = 0
	string = ''
	l = ''
	contPar = 0
	while((l!= ',' and len(a)!= 0)or contPar != 0):
		if(len(a)!= 0):
			l = a.pop(0)
			if(l==')' and len(a)==0):
				pass
			else:
				if(l=='('):
					contPar +=1
				if(l!=',' or contPar != 0):
					string = string+l
				cont = cont + 1
				if(l == ')'):
					contPar -=1
	return string



def solve():
	global matrix,numH,conver,already
	listaParejas = list()
	already = list()
	for i in range(numH):
		for j in range(i+1,numH):
			if(i!=j):
				one, two = matrix[i][:],matrix[j][:]
				if(isLowerCase(one[0])):
					if(one[1]=='('):
						one.pop(0)
						one.pop(0)
						if(isLowerCase(two[0])):
							if(two[1]=='('):
								two.pop(0)
								two.pop(0)
								while(len(one)!= 0):
									string1 = makeString(one)
									string2 = makeString(two)
									check = list(string2)
									if(isVariable(check[0])):
										listaParejas.append((string2,string1))
									else:
										listaParejas.append((string1,string2))
	solve2(listaParejas)

def solve2(listaParejas):
	global conver,already
	i = 0
	while(i !=len(listaParejas)):
		check = list(listaParejas[i][0])
		if(isVariable(check[0]) and listaParejas[i][0] not in already):
			conver.append(listaParejas[i])
			already.append(listaParejas[i][0])
			listaParejas.remove(listaParejas[i])
		else:
			i = i +1
	#print("Resultado-------------",conver,listaParejas,already)
	if(len(listaParejas)==0):
		print("analysis inconclusive on "+name)
	else:
		print(name+" is a Starflyer agent")



		
def main():
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
