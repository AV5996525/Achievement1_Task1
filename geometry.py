#Name:                  geometry.py
#Author:                AJ Varatharajan
#Date Created:          January 1, 2023
#Date Last Modified:    February 2, 2023

#Purpose
#
#This program will allow the user to calculate the area and perimeter of the following shapes:
# - Circle
# - Rectangle
# - Triangle
#User will be able to exit the program and will be notified if their response is invalid.
#Finally, the program will out each calculation and express them in the correct unit.
print("Welcome to the Geometry Calculator")
shapeSelection = input("1. Calculate the Area of a Circle \n2. Calculate the Area of a Rectangle \n3. Calculate the Area of a Triangle \n4. Quit") #Displaying user selection and accepting input from 1 to 4
shapeSelection = int(shapeSelection)        #Converting user input into integer value
if shapeSelection == 1 or shapeSelection == 2 or shapeSelection == 3 or shapeSelection == 4 :    #Condition for if the integer value meets the required input of 1 to 4.
    if shapeSelection == 1: #Circle selection
        import math         #Importing math to utilize pi to calculate circumfrence and area of a circle
        pi = (math.pi)      #Assigning pi to a variable    
        cirDiam = float(input("Enter the diameter of the circle:"))                 #User input and converting input into float value
        cirRad = (cirDiam/2)                                                        #Calculation the radius
        cirCircum = (pi*2*cirRad)                                                   #Performing calculations for circumfrence
        cirArea = (pi)*(cirRad**2)                                                  #Calculation area
        print("The circumfrence is" + str(cirCircum) + " cm." + " The area of circle is " + str(cirArea) + " cm².")  #Displaying calculations and converting float values into a string
    if shapeSelection == 2 :                                                                 #Rectangle selection
        rectWidth = float(input("Enter width of rectangle"))                                #User input and converting input into float value
        rectLength = float(input("Enter length of rectangle"))                              #User input and converting input into float value
        rectPerm = ((2*rectWidth)+(2*rectLength))                                           #Calculating perimeter
        rectArea = (rectWidth*rectLength)                                                   #Calculating area    
        print("The perimeter of the rectangle is " + str(rectPerm) + " cm." + " The area of the rectangle is " + str(rectArea) + " cm².")               #Displaying calculations and converting float values into a string
    if shapeSelection == 3 :                                                             #Triangle selection
        triWidth = float(input("Enter the triangle base"))                               #User input and converting input into float value    
        triLength = float(input("Enter the triangle height"))                            #User input and converting input into float value
        triSideA = float(input("Enter the first length of the triangle"))                #User input and converting input into float value
        triSideB = float(input("Enter the second length of the triangle"))               #User input and converting input into float value
        triSideC = float(input("Enter the third length of the triangle"))                #User input and converting input into float value
        triArea = ((triWidth*triLength)/2)                                               #Calculating area  
        triPerm = (triSideA + triSideB + triSideC)                                       #Calculating perimeter
        print("The perimeter of the triangle is " + str(triPerm) + " cm." + " The traingle area is " + str(triArea) + " cm².")      #Displaying calculations and converting float values into a string
    if shapeSelection == 4 :                                                #Quiting the application
        print("Have a great day, please come back again")    
        exit    
else :                                                                      #Condition for invalid user input
    print("Enter a valid response from 1 to 4")

