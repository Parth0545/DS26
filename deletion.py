class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
start=Node(10)
start.next=Node(20)
start.next.next=Node(30)

print("Original Linked List ")
temp=start
while temp is not None:
     print(temp.data,end=" -> ")
     temp=temp.next
     
print("None")

#deletion from beginning 
if start is None:
    print("linked list is empty")
else:
    temp=start
    start=start.next
    del temp
    
print("Linked List after deletion")
temp=start
while temp is not None:
    print(temp.data,end=" -> ")
    temp=temp.next
    
print("None")