# Maximum sum square sub-matrix of size k*k

import numpy as np


# a,b,c=m[:k,:k],m[:k,1:1+k],m[:k,2:2+k]
# d,e,f=m[1:k+1,:k],m[1:k+1,1:k+1],m[1:k+1,2:2+k]
# g,h,i=m[2:k+2,:k],m[2:k+2,1:k+1],m[2:k+2,2:2+k]
# print(a)
# print(b)
# print(c)

# print(d)
# print(e)
# print(f)

# print(g)
# print(h)
# print(i)

def find(k,m):
  m=np.matrix(m)
  inc=len(m)-k
  #print(inc)
  i=0

  l=[]
  for i in range(inc+1):
    l.append(m[i:k+i,:k])
    l.append(m[i:k+i,1:k+1])
    l.append(m[i:k+i,2:k+2])

  max=0
  maxt=[[0 for i in range(3)] for j in range(0,3)]
  #print(maxt)
  for a in l:
    #print(a)
    if(max<np.sum(a)):
      max=np.sum(a)
      maxt=a

  print(maxt)
    


m=[[0,0,0,0,0],
[1,1,1,0,0],
[1,1,1,0,0],
[1,1,1,0,0],
[0,0,0,0,0]]

k=3

find(k,m)
