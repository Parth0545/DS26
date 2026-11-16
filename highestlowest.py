arr=[10,20,30,40,50]
highest=arr[0]
lowest=arr[0]
for i in range(len(arr)):
    if(arr[i]>highest):
        highest=arr[i]
    if(arr[i]<lowest):
        lowest=arr[i]
        
print("highest",highest)

print("lowest",lowest)