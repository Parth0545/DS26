n=int(input("enter a number"))
set=n
sum=0
while n!=0:
    digit=n%10
    sum=sum + digit*digit*digit
    n=n//10

if sum==set:
    print("armstrong number")
else:
    print("not armstrong number")