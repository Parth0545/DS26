class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def MergeTwoLists(List1, List2):
    dummy = ListNode(-1)
    current = dummy

    while List1 and List2:
        if List1.val < List2.val:
            current.next = List1
            List1 = List1.next
            print("List1 is merged")
        else:
            current.next = List2
            List2 = List2.next
            print("List2 is merged")

        current = current.next

    current.next = List1 or List2

    return dummy.next
def display(head):
    while head:
        print(head.val,end="->")
        head=head.next
    print("None")
List1=ListNode(1)
List1.next=ListNode(2)
List1.next.next=ListNode(4)
List2=ListNode(1)
List2.next=ListNode(3)
List2.next.next=ListNode(4)
result=MergeTwoLists(List1,List2)
print("Merged linked list")
display(result)