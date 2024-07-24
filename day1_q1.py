cost_apple=15
cost_ban10ana=4
cost_orange=5
# no of fruits
print("enter no of apples")
no_apple=int(input())
print("enter no of banana")
no_banana=int(input())
print("enter no of oranges")
no_orange=int(input())
print("enter the amount given by the mother")
print_given=int(input())
sum=(no_apple*cost_apple)+(no_banana*cost_banana)+(no_orange*cost_orange)
if(sum<= print_given) :
    print("not cheated")
else:
    print("cheated")