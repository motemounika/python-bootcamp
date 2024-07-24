#check how many vowels are in a string
str=input()
vowels='a','e','i','o','u'
count=0
i="hello world"
for i in str:
    if(i in vowels):
        count+=1
print(count) 