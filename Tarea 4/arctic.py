from sys import stdin
import math

#Nombre: Juan Sebastian Rivera
#Codigo: 5498445
#Codigo tomado de la pagina del prof. Camilo Rocha (Kruskal - lecture 18)
#Trabajado con Maria P Carrero y Carlos Arboleda

class dforest(object):

  def __init__(self,size=100):
    """create an emtpy forest"""
    self.__parent = [ i for i in range(size) ]
    self.__size = [ 1 for i in range(size) ]
    self.__rank = [ 0 for i in range(size) ]
    
  def __str__(self):
    """return the string representation of the forest"""
    return str(self.__parent)

  def __len__(self):
    """return the number of elements in the forest"""
    return len(self.__parent)
  
  def __contains__(self,x):
    """return if x is an element of the forest"""
    return 0 <= x < len(self)

  def find(self,x):
    """return the representative of the tree of x"""
    assert x in self
    if self.__parent[x]!=x:
      self.__parent[x] = self.find(self.__parent[x])
    return self.__parent[x]

  def union(self,x,y):
    """make the union of the trees of x and y"""
    assert x in self and y in self
    rx,ry = self.find(x),self.find(y)
    if rx!=ry:
      nx,ny = self.__rank[rx],self.__rank[ry]
      if nx<=ny:
        self.__parent[rx] = ry
        self.__size[ry] += self.__size[rx]
        if nx==ny: self.__rank[ry]+=1
      else:
        self.__parent[ry] = rx
        self.__size[rx] += self.__size[ry]
        
  def size(self,x):
    """return the size of the tree of x"""
    assert x in self
    return self.__size[self.find(x)]

def kruskal(G,estaciones):
  edges = list()
  for i in range(len(G)):               
    for v,w in G[i]:
    	if(w != -1):
    		edges.append((i,v,w))
  edges.sort(key=lambda x: x[2])        
  df = dforest(len(G))
  i = 0
  casos = 0
  while i!=len(edges):
    u,v,w = edges[i]
    if df.find(u)!=df.find(v):
      df.union(u,v)
      casos = casos + 1
      if casos == estaciones:
      	return w
    i += 1



def main():
	line = stdin.readline().strip()
	cont = 0
	while cont < int(line):
		line1 = stdin.readline().strip().split()
		cont2 = 0
		lista = list()
		while cont2 < int(line1[1]):
			line2 = stdin.readline().strip().split()
			lista.append([int(line2[0]),int(line2[1])])
			cont2 = cont2 + 1
		lista2 = [ [(i,-1) for i in range(len(lista))]  for i in range(len(lista))]
		for i in range(len(lista)):
			j = i +1
			for w in range(j,len(lista)):
				distancia = math.hypot(lista[i][0]-lista[w][0],lista[i][1]-lista[w][1])
				lista2[i][w]=[w,distancia]
		cont = cont + 1
		ans = kruskal(lista2,int(line1[1])-int(line1[0]))
		print('{:.2f}'.format(ans))


main()