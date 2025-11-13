varside1=float(input("Enter first side of the triangle:"))
varside2=float(input("Enter first side of the triangle:"))
varside3=float(input("Enter first side of the triangle:"))
varsemiperi=(varside1+varside2+varside3)/2
varareatri=(varsemiperi*(varsemiperi-varside1)*(varsemiperi-varside2)*(varsemiperi-varside3))**0.5
print("The area of the triangle is %0.3f"%varareatri)
