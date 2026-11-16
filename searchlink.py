a=[25,83,4,2,75,16,45,5,99,1]

a.sort()

print("sorted list",a)
key=int(input("enter search key"))

low=0
high=len(a)-1
found=False

while low<= high:
    mid=(low+high)//2
    
    if a[mid]==key:
        print("search key found at index",mid)
        found=True
        break
    elif key>a[mid]:
        low=mid+1
    else:
        high=mid-1
        
if found==False:
    print("search key not found")
    