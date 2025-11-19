Varrows= int(input("Enter the number of rows: "))

Vark=0
VarCnt=0
VarCnt1=0

for j in range(1,Varrows+1):
    for Varspace in range(1, (Varrows-j)+1):
        print(" ",end="")
    VarCnt+=1
    
    while Vark!=((2*j)-1):
        if VarCnt<=Varrows-1:
            print(j+Vark,end="")
            VarCnt +=1
        else:
            VarCnt1+=1
            print(j+Vark-(2*VarCnt+1), end=" ")
            Vark+=1
            VarCnt1=VarCnt=Vark=0
            print()

