def funcadd(Varx,Vary,Varz):
    return Varx+Vary+Varz
def funcsub(Varx,Vary,Varz):
    return Varx-Vary-Varz
def funcmul(Varx,Vary,Varz):
    return Varx*Vary*Varz
def funcadd(Varx,Vary):
    return Varx/Vary

print("Please select the operator:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    Varch=input("Enter the choice(1/2/3/4):")
    
    if Varch in ('1','2','3'):
        Varno1=float(input("Enter first number"))
        Varno2=float(input("Enter second number"))
        Varno3=float(input("Enter third number"))
    elif Varch in ('4'):
            Varno1=float(input("Enter first number"))
            Varno2=float(input("Enter second number"))
    if Varch=='1':
        print(Varno1,"+",Varno2,"+",Varno3,"=", funcadd(Varno1,Varno2,Varno3))
        if Varch=='2':
            print(Varno1,"-",Varno2,"-",Varno3,"=", funcsub(Varno1,Varno2,Varno3))
            if Varch=='3':
                print(Varno1,"*",Varno2,"*",Varno3,"=", funcmul(Varno1,Varno2,Varno3))
                if Varch=='4':
                    print(Varno1,"/",Varno2,"=", funcdivide(Varno1,Varno2))
                break
            else:
                print("Invalid Input")
                
