# Nicholas Handberg, Final Exam Part 2, 2/22/2021
# Topics: Objects, Inheritance
# Create a program that randomly creates 15 shapes and have the shapes draw themselves.

import random                                                                                           # Imports the random module
from turtle import Turtle                                                                               # Imports Turtle from the turtle module

class Shape():                                                                                          # Creates the superclass Shape
    
    turtle = Turtle()                                                                                   # Initializes the class variable 'turtle' to Turtle() object
        
class Circle(Shape):                                                                                    # Creates the subclass Circle which inherits from the superclass Shape
    def __init__(self, center, radius):                                                                 # Defines the constructor method and initializes the data attributes center and radius to the passed in values
        self.center = center
        self.radius = radius
    def get_area(self):                                                                                 # Defines the get_area() method which returns the result of the area calculation
        return 3.14* self.radius*self.radius
    def draw(self):                                                                                     # Defines the draw() method which draws the circle using the center and radius data attributes
        Shape.turtle.penup() 
        Shape.turtle.setposition(self.center[0], self.center[1] - self.radius)
        Shape.turtle.pendown() 
        Shape.turtle.circle(self.radius) 
        Shape.turtle.penup()   


class Rectangle(Shape):                                                                                 # Creates the Rectangle subclass which inherits from the Shape superclass
    def __init__(self, up_left, low_right):                                                        # Defines the contructor method and initializes the data attributes up_left and low_right to the passed in values
        self.up_left = up_left
        self.low_right = low_right
    def get_area(self):                                                                                 # Defines the get_area() method which returns the result of the area calculation
        return abs(self.up_left[0] - self.low_right[0]) * abs(self.up_left[1] - self.low_right[1]) 
    def draw(self):                                                                                     # Defines the draw() method which draws the rectangle using the up_left and low_right data attributes
        Shape.turtle.penup() 
        Shape.turtle.setposition(self.up_left)
        Shape.turtle.pendown() 
        Shape.turtle.goto(self.low_right[0],self.up_left[1])
        Shape.turtle.goto(self.low_right)
        Shape.turtle.goto(self.up_left[0],self.low_right[1])
        Shape.turtle.goto(self.up_left)
        Shape.turtle.penup() 

class RightTriangle(Shape):                                                                             # Creates the RightTriangle subclass which inherits from the Shape superclass
    def __init__(self, point_a, point_b):                                                               # Defines the contructor method and initializes the data attributes point_a and point_b to the passed in values
        self.point_a = point_a
        self.point_b = point_b
    def get_area(self):                                                                                 # Defines the get_area() method which returns the result of the area calculation
        base = abs(self.point_a[0] - self.point_b[0])
        height = abs(self.point_a[1] - self.point_b[1])
        return 0.5*base*height
    def draw(self):                                                                                     # Defines the draw() method which draws the right triangle using the point_a and point_b data attributes
        Shape.turtle.penup() 
        Shape.turtle.setposition(self.point_a)
        Shape.turtle.pendown() 
        Shape.turtle.goto(self.point_b)
        Shape.turtle.goto(self.point_a[0],self.point_b[1])
        Shape.turtle.goto(self.point_a)
        Shape.turtle.penup() 

def random_shapes(count):                                                                               # Defines the random_shapes() function with count as a parameter
    def random_point():                                                                                 # Defines the random_point() function which returns a tuple of 2 random integers
        return (random.randint(-200,200), random.randint(-200,200))
    shapes = []                                                                                         # Creates the empty list shapes
    for i in range(1, count+1):                                                                         # For loop for the amount in the passed in parameter count
        
        shape_type = random.randint(1, 3)                                                               # Choses a random integer from 1-3 and stores it in shape_type
        
        if shape_type == 1:                                                                             # If statement checks if the value stored in shape_type is 1
            shapes+=[Circle(random_point(), random.randint(1,200))]                                     # Calls the Circle class passing the returned value from random_point() function and a random positive integer and adds the return to the shapes list
        elif shape_type == 2:                                                                           # If statement checks if the value stored in shape_type is 2
            shapes+=[Rectangle(random_point(), random_point())]                                         # Calls the Rectangle class passing the 2 returned values from random_point() function and adds the return to the shapes list
        else:                                                                                           # Else statement if shape_type is not a 1 or 2
            shapes+=[RightTriangle(random_point(), random_point())]                                     # Calls the RightTriangle class passing the 2 returned values from random_point() function and adds the return to the shapes list
    return shapes                                                                                       # Returns the shapes list

def main():                                                                                             # Defines the main() function
    shapes = random_shapes(15)                                                                          # Calls the random_shapes function with the value of 15 as an argument. Stores the returned list in shapes
    total_area = 0                                                                                      # Sets the total_area to 0
    for s in shapes:                                                                                    # For loop that loops for the number of elements in the shapes list
        s.draw()                                                                                        # Calls the respective shape's draw() method
        total_area += s.get_area()                                                                      # Calls the respective shape's get_area() method and adds the returned value to total_area

    input('Press <enter> when done viewing')
    print(f"Total area = {total_area:.2f}")                                                             # Prints the total area of the 15 shapes
    

main()                                                                                                  # Calls the main() function
