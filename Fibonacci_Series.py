VarNum1=int(input("Enter a number of terms for Fibonacci Series:"))
Varn1,Varn2=0,1
VarCount=0
if VarNum1<=0:
            print("Please enter a positive number only")
elif VarNum1==1:
            print("Fibonacci Sequence uptill",Varnum1,":")
            print(Varn1)
else:
            print("The Fibonacci Sequence:")
            while VarCount<VarNum1:
                        print(Varn1)
                        VarTemp=Varn1+Varn2
                        Varn1=Varn2
                        Varn2=VarTemp
                        VarCount+=1
                        
