VarNum=int(input("Enter a number:"))
VarFact=1
if VarNum<0:
    print("Ohh sorry,Factorial does not exist for negative numbers")
elif VarNum==0:
        print("The Factorial of 0 is 1")
else:
        for j in range(1,VarNum+1):
            VarFact=VarFact*j
            print("The Factorial of", VarNum,"is", VarFact)
