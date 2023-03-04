def number_pattern(n):
    for i in range(1,n,1):
        for j in range(1,i+1,1):
            print(i,end=" ")
        print("\r")
a = int(input("Enter the number upto which pattern is to be printed: "))
number_pattern(a)
