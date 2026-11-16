a=[1,2,3,4]
print("the array is",end="")
for i in range(0,4):
    print(a[i],end="")
a.insert(4,5)
print("after in insertion",end="")
for i in range(0,5):
    print(a[i],end="")