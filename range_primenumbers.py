VarMin=int(input("Enter the start range:"))
VarMax=int(input("Enter the end range:"))
print("Prime numbers in between",VarMin,"and",VarMax,"are:")
for Varj in range(VarMin,VarMax+1):
    if(Varj>1):
        for j in range(2,Varj):
            if(Varj%j)==0:
                break
            else:
                print(Varj)
