#print a leap year between a given range
year1=int(input())
year2=int(input())
for i in range(year1,year2+1):
      if(i%4==0 or i%4==0 and i%100!=0):
            print(i,end=" ")

           