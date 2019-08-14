##Decimal to Binary


# from collections import deque

# s=input()
# if(s[::1]==s[::-1]):
#   print("Palindrome")
# else:
#   print("Not")


# def dividBy2(n):
#   s=""
#   while(n>0):
#     s=s+(str(n%2))
#     n=n//2
#   print(s)
#   print(s[::-1])

# dividBy2(30)

#############################################################

##TowerOfHanoi

# def listsum(numList):
#    if len(numList) == 1:
#         return numList[0]
#    else:
#         return numList[0] + listsum(numList[1:])

# print(listsum([1,3,5,7,9]))

# def moveTower(height,fromT,toT,withT):
#   if height>=1:
#     moveTower(height-1,fromT,withT,toT)
#     moveDisk(fromT,toT)
#     moveTower(height-1,withT,toT,fromT)
    
# def moveDisk(fp,tp):
#   print(fp,"->",tp,end="\n")

# moveTower(12,"A","B","C")







#############################################################
##MinNumberOfCoinsForGivenDenominations

# import sys

# def minCoins(coins,V):
#   if(V==0):
#     return 0

#   res=sys.maxsize
  
#   for i in coins:
#     if(i<=V):
#         sub_res=minCoins(coins,V-i)
#         print(sub_res)
#         if(sub_res + 1 < res):
#           res=sub_res+1
#           #print(res)

#   return res

# coins=[10,20]
# V=200
# print(minCoins(coins,V))


#############################################################
# def pascal_triangle(n):
#    trow = [1]
#    y = [0]
#    for x in range(n):
#       print(trow)
#       print(list(zip(trow+y,y+trow)))
#       trow=[l+r for l,r in zip(trow+y, y+trow)]
  
# pascal_triangle(6)

#############################################################

##Knapsack

# from collections import deque

# weight=[2,3,4,5,9]
# value=[3,4,8,8,10]
# per_item_val=deque([i/j for i,j in zip(weight,value)])
# print(per_item_val)
# w=20
# new_w=0
# val=0
# while(new_w<=w):
#   i=per_item_val.index(max(per_item_val))
#   print(i)
#   per_item_val[i]=0
  
  
#   new_w=new_w+weight[i]
#   if(new_w<=w):
#     val=val+value[i]
#   else:
#     break

# print(val)

#############################################################

##BinarySearch

# def binarySearch(alist,el):
#   mid=len(alist)//2
#   if len(alist)==0:
#     return False

#   else:
#     if(alist[mid]==el):
#       return True
#     if(el>alist[mid]):
#       return binarySearch(alist[mid:],el)
#     else:
#       return binarySearch(alist[:mid],el)
    
# a=[1,2,3,4,6,7,9]
# print(binarySearch(a,6))
# print(binarySearch(a,0))

#############################################################