varnum=int(input("Enter a number:"))
VarFact=1
if varnum<0:
    print("Ohh sorry, Factorial does not exist for a negative numbers")
elif varnum==0:
        print("The Factorial of 0 is 1")
else:
        for j in range(1,varnum+1):
    VarFact=VarFact*j
        print("The Factorial of",varnum,"is",VarFact)
