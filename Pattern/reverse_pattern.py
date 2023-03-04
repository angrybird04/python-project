def number_pattern(n):
    for i in range(n,0,-1):
        c=0
        for j in range(c,i,1):
            print(c,end=" ")
        print("\r")
a = int(input("Enter the number upto which pattern is to be printed: "))
number_pattern(a)
