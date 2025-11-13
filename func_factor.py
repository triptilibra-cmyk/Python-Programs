def fact_user(fac):
    print("The Factors of",fac,"are:")
for j in range(1,fac+1):
    if fac%j==0:
        print(j)
        Varnm=int(input("Enter a number to see the factors:"))
        fact_user(Varnm)
