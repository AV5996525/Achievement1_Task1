#Make sure follow proper format Author date purpose
#
#
#
print("Welcome to the Geometry Calculator")
shapeSelection = input("1. Calculate the Area of a Circle \n2. Calculate the Area of a Rectangle \n3. Calculate the Area of a Triangle \n4. Quit")
shapeSelection = int(shapeSelection)
if shapeSelection == 1 or shapeSelection == 2 or shapeSelection == 3 or shapeSelection == 4 :
    if shapeSelection == 1:
        cirWidth = float(input("Enter the width of the circle:"))
        cirLength = float(input("Enter the length of the circle"))
    if shapeSelection == 2 :
        rectWidth = float(input("Enter width of rectangle"))
        rectLength = float(input("Enter length of rectangle"))
    if shapeSelection == 3 :
        triWidth = float(input("Enter the triangle width"))
        triLength = float(input("Enter the triangle length"))        
else :
    print("Enter a valid response from 1 to 4")

