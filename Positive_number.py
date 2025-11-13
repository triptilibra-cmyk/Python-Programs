VarNum=int(input("Enter a number:"))
if VarNum<0:
    print("Enter a positive number")
else:
    VarSum=0
while(VarNum>0):
    VarSum+=VarNum
    print("The VarNum is:",VarNum,"The value of VarSum is:",VarSum)
