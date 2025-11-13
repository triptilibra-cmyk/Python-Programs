def fact_user(Varnum):
    print("The factors of",Varnum,"are:")
    for j in range(1,Varnum+1):
        if Varnum%j==0:
            print(j)
            varnm=int(input("Enter a number to see the factors:"))
            fact_user(varnm)
