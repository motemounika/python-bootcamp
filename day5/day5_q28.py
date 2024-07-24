str=input()      
check="0123456789"             
sum=0
for i in (str):
    if(i in check):
        sum+=int(i)
print(sum)