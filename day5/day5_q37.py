#write a code to print capital letters in a string
str=input()
for i in str:
    if(ord(i)>65 and ord(i)<97):
        print(i,end=" ")