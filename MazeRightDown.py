M=[[1,8,21,7],
[19,17,10,20],
[2,18,23,22],
[14,25,4,13]]

x=1
R=len(M)
C=len(M[0])
y=[[0,0]]
i=0
j=0

while i<4 and j<4:
      if i==3:
        a=3
      else:
        a=i+1
      if j==3:
        b=3
      else:
        b=j+1      
  
      if(M[a][j]<M[i][b]):
            y.append([a,j])
            if(i<3):
              i=i+1
            else:
              i=3
              j=j+1
            
            if(x<M[a][j]):
              x=M[a][j]
              print(x)
              print(y)
          

      elif(M[a][j]>M[i][b]):
            y.append([i,b])
            if(j<3):
              j=j+1
            else:
              j=3
              i=i+1
            if(x<M[i][b]):
              x=M[i][b]
              print(x)
              print(y)


              

          
