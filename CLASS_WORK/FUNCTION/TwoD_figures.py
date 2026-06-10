#program to implment 2d figures using functions
#function to calculate area and perimeter of rectangle and square
def rectangle(length, breadth): 
    #calculate area of rectangle 
    area = length * breadth
    #calculate perimeter of rectangle       
    perimeter = 2 * (length + breadth)
    #return area and perimeter
    return area, perimeter  

#---------------------------------------------------------
#For square
def square(side):
    #calculate area of square
    area = side * side
    #calculate perimeter of square
    perimeter = 4 * side
    #return area and perimeter
    return area, perimeter

#----------------------------------------------------------
#for Circle
def circle(radius):
    #calculate area of circle
    area = 3.14
    #calculate perimeter of circle
    perimeter = 2 * 3.14 * radius
    #return area and perimeter
    return area, perimeter