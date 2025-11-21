Varrows=int(input("Enter the number of rows for Floyd's Triangle: "))
Varnum=1
for j in range(1, Varrows+1):
    for j1 in range(1, j+1):
        print(Varnum, end="")
        Varnum+=1
        print()
