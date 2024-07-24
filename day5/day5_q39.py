#write a code ABC,4
#OP:EFG
str=input()
for i in str:
    if(ord(i)==65 or ord(i)==66 or ord(i)==67):
       print(chr(ord(i)+4),end=" ")