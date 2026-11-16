marks=[[75,80,65,90],
       [60,70,85,75],
       [88,92,78,85]]

print("total marks")
for i in range(3):
    total=0
    for j in range(4):
        total+=marks[i][j]
    print("student",i+1,"+",total)