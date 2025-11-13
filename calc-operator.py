def funcadd(varx, vary):
    return varx+vary

def funcsub(varx, vary):
    return varx-vary

def funcmul(varx, vary):
    return varx*vary

def funcdivide(varx, vary):
    return varx/vary

print("Please select the operator:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    Varch=input("Enter the choice(1/2/3/4):")

if Varch in('1','2','3','4'):
    Varno1=float(input("Enter first number:"))
    Varno2=float(input("Enter second number:"))
    
if Varch=='1':
    print(Varno1,"+",Varno2,"=", funcadd(Varno1,Varno2))

elif Varch=='2':
    print(Varno1,"-",Varno2,"=", funcsub(Varno1,Varno2))

elif Varch=='3':
    print(Varno1,"*",Varno2,"=", funcmul(Varno1,Varno2))

elif Varch=='4':
    print(Varno1,"/",Varno2,"=", funcdivide(Varno1,Varno2))
break

else:
    print("invalid input")
    
