class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class stack:
    def __init__(self):
        self.top=None
        
    #PUSH operation
    def push(self,item):
        new_node=Node(item)
        new_node.next=self.top
        self.top=new_node
        print(item,"inserted")
        
    #POP operation
    def pop(self):
        if self.top is None:
            print("stack underflow")
        else:
            item=self.top.data
            self.top=self.top.next
            print("deleted element",item)
            
    #PEEK operations
    def peek(self):
        if self.top is None:
            print("stack is empty")
        else:
            print("top element",self.top.data)
    
    #DISPLAY operation
    
    def display(self):
        if self.top is None:
            print("stack is empty")
        else:
            temp=self.top
            print("stack elements")
            while temp is not None:
                print(temp.data)
                temp=temp.next
                
s=stack()
s.push(10)
s.push(20)
s.push(30)

s.display()
s.peek()
s.pop()
s.display()

                
        
        