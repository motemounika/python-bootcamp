#find maximum element in an array
my_list=list(map(int,input().split(" ")))
max=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>max):
        max=my_list[i]
print(max)