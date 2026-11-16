highest=marks[0][0]

for i in range(3):
    for j in range(4):
        if marks[i][j]>highest:
            highest=marks[i][j]
    print("highest marks",highest)