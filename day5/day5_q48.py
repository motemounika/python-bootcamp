n = int(input())
#print("UPPER TRIANGLE MATRIX")
#for i in range(n):
#    for j in range(n):
#        if(j>=i):
#            print("*", end = " ")
#        else:
#            print(" ", end = " ")
#    print()
#print()

print("LOWER TRIANGLE MATRIX")
for i in range(n):
    for j in range(n):
        if(j<=i):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
print()