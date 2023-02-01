#Make sure follow proper format Author date purpose
#
#
#
print("Welcome to the Geometry Calculator")
shapeSelection = input("1. Calculate the Area of a Circle \n2. Calculate the Area of a Rectangle \n3. Calculate the Area of a Triangle \n4. Quit")
shapeSelection = int(shapeSelection)
if shapeSelection == 1 or shapeSelection == 2 or shapeSelection == 3 or shapeSelection == 4 :
    if shapeSelection == 1:
        import math
        pi = (math.pi)
        cirDiam = float(input("Enter the diameter of the circle:"))
        cirRad = (cirDiam/2)
        cirCircum = (pi*2*cirRad)
        cirArea = (pi)*(cirRad**2)
        print("the circumfrence is" + str(cirCircum) + "the area of circle is" + str(cirArea) + " cm².")  
    if shapeSelection == 2 :
        rectWidth = float(input("Enter width of rectangle"))
        rectLength = float(input("Enter length of rectangle"))
        rectPerm = ((2*rectWidth)+(2*rectLength))
        rectArea = (rectWidth*rectLength)
        print("The perimeter of the rectangle is " + str(rectPerm) + " cm." + " The area of the rectangle is " + str(rectArea) + " cm².")
    if shapeSelection == 3 :
        triWidth = float(input("Enter the triangle base"))
        triLength = float(input("Enter the triangle height"))   
        triSideA = float(input("Enter the first length of the triangle"))
        triSideB = float(input("Enter the second length of the triangle"))
        triSideC = float(input("Enter the third length of the triangle"))
        triArea = ((triWidth*triLength)/2)
        triPerm = (triSideA + triSideB + triSideC)
        print("The perimeter of the triangle is " + str(triPerm) + " cm." + "The traingle area is " + str(triArea) + " cm².")
    if shapeSelection == 4 :
        print("Have a great day, please come back again")    
        exit    
else :
    print("Enter a valid response from 1 to 4")

