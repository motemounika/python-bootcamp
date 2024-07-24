height_of_x=int(input())
height_of_y=int(input()) 
weight_of_x=int(input())
weight_of_y=int(input())
x_selected=0 
y_selected=0
if (height_of_x ==140 and weight_of_x%2==0):
    x_selected+=1
    
if((height_of_y<148 and height_of_y>118) and weight_of_y%7==0):
    y_selected+=1
    
if(y_selected==1 and x_selected ==1):
    print("x,y and z will meet in airplane")
else:
    print("not meet")