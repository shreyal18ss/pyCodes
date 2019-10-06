m=[[1,2,3,400],[1,20,30,2],[4,4,4,4],[5,5,50,100]]
k=3
l=[]
for i in range(len(m)):
  for j in range(len(m[0])):
    try:
      sum=0
      for x in range(k):
        for y in range(k):
          sum+=m[i+x][j+y]
          l.append(sum)
    except:
      continue
print(l)
print(max(l))
