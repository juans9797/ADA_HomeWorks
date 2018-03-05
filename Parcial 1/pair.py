from sys import stdin
import math

#Nombre: Juan Sebastian Rivera
#Codigo de estudiante: 5498445
#Basado en el template de la primera tarea
#Discutido con: Juan Sebastian Quiceno, Maria Paula Carrero, Juan Fernando Escobar

EPS,points = 1e-9,None

def distancia(a,b):
  dist = math.hypot((a[0]-b[0]),(a[1]-b[1]))
  return dist


def solve(low,hi):
  global points
  ans = float('inf')
  alt = []
  if hi-low <= 1:
    ans = float('inf')
  elif hi-low ==2:
    ans = distancia(points[low],points[low+1])
  elif hi - low ==3:
    d1 = distancia(points[low],points[low+1])
    d2 = distancia(points[low+1],points[low+2])
    d3 = distancia(points[low],points[low+2])
    ans = min(d1,d2,d3)
  else:
    mid = low + ((hi-low)>>1)
    ans1 = solve(low,mid)
    ans2 = solve(mid,hi)
    ans = min(ans1,ans2)
    for i in range(low,hi):
      if abs(points[mid][0]-points[i][0]) < ans:
        alt.append(points[i])
       
    for j in range(len(alt)):
      for w in range(j+1,len(alt)):
        d = distancia(alt[j],alt[w])
        ans = min(d,ans)

  return ans





def main():
  global points
  n = int(stdin.readline())
  while n!=0:
    points = list()
    for i in range(n):
      tok = stdin.readline().split()
      points.append((float(tok[0]),float(tok[1])))
    points.sort(key=lambda x: (x[0], x[1]))
    if n==1:
      print("INFINITY")
    else:
      ans = solve(0,n)
      if ans < 10000:
        print('{:.4f}'.format(ans))
      else:
        print("INFINITY")
    n = int(stdin.readline())

main()
