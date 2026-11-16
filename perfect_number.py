n=int(input("enter the number"))
set_sum=0
for i in range(1,n):
    if n%i==0:
        set_sum=set_sum+i
if set_sum==n:
    print("perfect number")
else:
    print("not perfect number")
    