from sys import stdin
#Nombre: Juan Sebastian Rivera
#Codigo de estudiante: 5498445
#Trabajado con Juan Fernando Escobar, Maria Paula Carrero
list1,list2,resultado = None,None,None
def topo(G,indeg):
	ans = list()
	cand = list()
	for u in range(len(indeg)):
		if indeg[u]==0:
			valor = chr(u+97)
			cand.append(valor)
	while len(cand) != 0:
		opcion = cand.pop()
		ans.append(opcion)
		for i in range(len(G)):
			if opcion == G[i][0]:
				letra = ord(G[i][1])-97
				indeg[letra] = indeg[letra]-1
				if indeg[letra]==0:
					cand.append(G[i][1])
	return ans


def topos(indeg,ans,contador):
	global list1,list2,resultado
	cand = list()
	for u in range(len(indeg)):
		if indeg[u]==0:
			valor = chr(u+97)
			cand.append(valor)
	anst = ans
	contador = contador+1
	for i in range(len(cand)):
		opcion = cand.pop()
		anst = ans + opcion
		if contador == len(list1):
			resultado.append(anst)
		else:
			indegtemp = indeg[:]
			letra = ord(opcion)-97
			indegtemp[letra] = indegtemp[letra]-1
			for i in range(len(list2)):
				if opcion == list2[i][0]:
					letra = ord(list2[i][1])-97
					indegtemp[letra] = indegtemp[letra]-1
			topos(indegtemp,anst,contador)


def main():
	global list1,list2,resultado
	line = "1"
	while line != "":
		tot = 0
		line = stdin.readline().strip()
		if line != "":
			indeg = list()
			list2 = list()
			cont = 0
			list1= [x for x in line.split() ]
			test= [-1 for x in range(26) ]
			line = stdin.readline().strip().split()
			list1.sort()

			for i in list1:
				letra = ord(i)-97
				test[letra]=0

			while cont < len(line):
				list2.append([line[cont],line[cont+1]])
				letra = line[cont+1]
				test[ord(letra)-97]=test[ord(letra)-97]+1
				cont = cont + 2
			resultado = list()
			topos(test,'',0)
			tot = len(resultado)
			if tot != 0:
				for i in range(1,tot+1):
					print(resultado[tot-i])
				print("")




main()