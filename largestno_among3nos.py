varnum1=float(input("Enter first number:"))
varnum2=float(input("Enter second number:"))
varnum3=float(input("Enter third number:"))
if(varnum1>=varnum2)and (varnum1>=varnum3):
    varlarge=varnum1
elif(varnum2>=varnum1)and (varnum2>=varnum3):
            varlarge=varnum2
else:
             varlarge=varnum3
             print("The largest number among all is:",varlarge)
