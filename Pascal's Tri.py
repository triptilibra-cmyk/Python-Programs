Varrows=int(input("Enter the number of rows for Pascal's Triangle: "))
Varcoef=1
for j in range(1, Varrows+1):
    for Varspace in range(1, Varrows-j+1):
        print(" ",end="")
        for j1 in range(0, j):
            if j1==0 or j==0:
                Varcoef=1
            else:
                Varcoef=Varcoef*(j-j1)//j1
                print(Varcoef, end="")
                print()
