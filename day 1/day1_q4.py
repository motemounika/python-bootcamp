n=int(input())
x=n 
rev=0
   while(n>0):
    r=n%10
rev=(10*rev)+r
n=n//10
print("the reverse of given number is",rev)
   if(rev==x):
    print("palindrome")
   else:
    print("not a palindrome")
    
   