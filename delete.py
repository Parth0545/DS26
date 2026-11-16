a=[2,1,3,5,4,5]
print("array  deletion",end="")
for i in range(0,3):
    print(a[i],end="")
a.pop(2)
print("after  deletion",end="")
for i in range(0,2):
    print(a[i],end="")
    