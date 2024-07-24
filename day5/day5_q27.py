#write a program to print unique characters in a string
vowel="aeiou"
consonent="bxdgsyshiupuxzcfa"
ans=" "
i="hello world"
inp=i.lower()
for i in inp:
    if(i not in ans):
        ans+=i
print(ans)
