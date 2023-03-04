for i in range(10,0,-2):
    for j in range(i,0,-1):
        if j<10:
            print("*",end="  ")
        else:
            print("*",end=" ")
    print("\r")