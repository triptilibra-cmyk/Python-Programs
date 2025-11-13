import calendar
while True:
    VarYear=int(input("Enter a year which is more than 2000:"))
    if VarYear>2000:
        VarMonth=int(input("Enter a month:"))
        print(calendar.month(VarYear,VarMonth))
        break
    else:
        print("Please enter a proper year:")
