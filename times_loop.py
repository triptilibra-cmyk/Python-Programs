varnum=int(input("Enter a number to check if it is Prime number:"))
if varnum>1:
    for j in range(2,varnum):
        if(varnum%j)==0:
            print(varnum,"is not a prime number")
            print(j,"times",varnum//j,"is",varnum)
            break
        else:
            print(varnum,"is a prime number")
    else:
                print(varnum,"is not a prime number")
