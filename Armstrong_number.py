VarNum=int(input("Enter a number:"))
VarSum=0
VarTemp=VarNum
while VarTemp>0:
    Vard=VarTemp%10
    VarSum+=Vard**3
    VarTemp//=10
    if VarNum==VarSum:
        print(VarNum,"is an Armstrong number")
    else:
            print(VarNum,"is not an Armstrong number")
