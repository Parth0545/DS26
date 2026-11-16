matrix=[
    [0,0,1],
    [0,2,0],
    [0,0,0]
]

zero=0
nonzero=0

for row in matrix:
    for element in row:
        if element==0:
            zero+=1
        else:
            nonzero+=1
            
if zero>nonzero:
    print("matrix is sparse")
else:
    print("matrix is not sparse")