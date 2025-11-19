Varrows=int(input("Enter the number of rows for Pyramid: "))

Vark=0

for j in range(1,Varrows+1):
    for Varspace in range(1,(Varrows-j)+1):
        print(end="")
        while Vark!=(2*j-1):
            print("* ",end="")
            Vark+=1
            
            Vark=0
            print()
