import calendar
while True:
    VarYear=int(input("Enter a year which is more than 2000:"))
    if VarYear>2000:
        VarMonth=int(input("Enter a month:"))
        if(VarMonth>=1)and(VarMonth<=12):
            print(calendar.month(VarYear,VarMonth))
        else:
            print("Sorry invalid month")
            break
    else:
        print("Please enter a proper year:")
