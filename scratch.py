    x = 6
y = ""
for i in range(6):
    for j in range(x-1):
        y = y + " "
    for k in range(6-x):
        y = y + "*"
    print(y)
    y = ""
