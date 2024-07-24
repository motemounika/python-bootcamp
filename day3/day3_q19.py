#find the elements that is present in k+N index
#k=3
#N=2
#3 6 8 4 6 2
#op:2
#------
##k=3
#N=4
#80 70 54 36 72
#op:error  
my_list=list(map(int,input().split(" ")))
k=int(input())
n=int(input())
if (len(my_list)<k+n):
 print(error)
for i in range(0,len(my_list)):
 print(my_list[k+n],end="")
 break

