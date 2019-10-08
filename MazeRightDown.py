
  
M=[[1,8,21,7],
[19,17,10,20],
[2,18,23,22],
[14,25,4,13]]
t=M[0][0]
x,y=0,0
w=t
print(t)
while(x<=3):
  try:
    if(M[x+1][y]<M[x][y+1]):
     x+=1
    elif(M[x+1][y]>M[x][y+1]):  
     y+=1
  except(IndexError):
    if(x<3):
      x+=1
    else:
      break
  t=M[x][y]
  print(t)
  w+=t
  
print(w)
