#write a program to print all the consonants count
str=input()
vowel="aeiou"
consonent="bcdnghjklmnpqrstvwxyz"
#count=0
ans=""
for i in (str):
    if(i in consonent):
        ans+=i
        #print(i,end=" ")
for i in (str):
    if(i in vowel):
        ans+=i
print(ans)
        #print(i,end=" ")
