import TwoD_figures
#function to calculate area and perimeter of rectangle 
length = int(input("Enter the length of the rectangle : "))
breadth = int(input("Enter the breadth of the rectangle : "))
#validate the length and breadth
if length < 0 or breadth < 0:
    exit("Length and breadth cannot be negative.")      
area= TwoD_figures.rectangle(length, breadth)[0]
perimeter = TwoD_figures.rectangle(length, breadth)[1]  
print("Area of the rectangle : ", area)
print("Perimeter of the rectangle : ", perimeter)   

#function to calculate area and perimeter of square
side = int(input("Enter the side of the square : "))
#validate the side
if side < 0:
    exit("Side cannot be negative.")
area = TwoD_figures.square(side)[0]
perimeter = TwoD_figures.square(side)[1]
print("Area of the square : ", area)
print("Perimeter of the square : ", perimeter)    


# create a prog which provides a menu to the user to select the two d figures (circle,rect,square) after selecting the figure user is again asked to provide the input of corresponding data for the figure after input of corresponding data again provide a menu to select the operation(area,perimeter) and as per the operation slect by user display the result of  operation the tak is repeat again and again until user slect the option to that figure

