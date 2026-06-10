#create a prog which provides a menu to the user to select the two d figures (circle,rect,square) after selecting the figure user is again asked to provide the input of corresponding data for the figure after input of corresponding data again provide a menu to select the operation(area,perimeter) and as per the operation slect by user display the result of  operation the tak is repeat again and again until user slect the option to that figure#

import TwoD_figures

from TwoD_figures import rectangle, square, circle

while True:
    print("--- 2D FIGURES MENU ---")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 4:
        print("Exiting the program.")
        exit()
#-----------------------------------------------------------------------------------
     #circle
    if choice == 1:
     
     radius = float(input("Enter radius: "))
    

    while True:
        print("\n1. Area")
        print("2. Perimeter")
       

        op = int(input("Enter operation: "))

        area, perimeter = TwoD_figures.circle(radius)

        if op == 1:
            print("Area of Circle =", area)

        elif op == 2:
            print("Perimeter of Circle =", perimeter)

        else:
            print("Invalid choice!")
     #----------------------------------------------------------------------------------
        # Rectangle
        if choice == 2:
         length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))

        while True:
            print("\n1. Area")
            print("2. Perimeter")

            op = int(input("Enter operation: "))

            area=TwoD_figures.rectangle(length, breadth)[0]
            perimeter = TwoD_figures.rectangle(length, breadth)[1]

            if op == 1: 
                print("Area of Rectangle =", area)
            elif op == 2:
                print("Perimeter of Rectangle =", perimeter)


            else:             print("Invalid choice!")
#----------------------------------------------------------------------------------
           #square
            if choice == 3: 
             side = float(input("Enter side: "))

            while True:
             print("\n1. Area")
             print("2. Perimeter")

             op = int(input("Enter operation: "))

             area = TwoD_figures.square(side)[0]
             perimeter = TwoD_figures.square(side)[1]

             if op == 1:
                print("Area of Square =", area)
             elif op == 2:
                print("Perimeter of Square =", perimeter)

             else:
                print("Invalid choice!")

#----------------------------------------------------------------------------------