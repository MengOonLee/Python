# Use Paper, Triangle, Oval and Rectangle classes for the shapes file.
from shapes import Paper, Triangle, Rectangle, Oval
# Create an instance of a Paper object.
paper = Paper()
# Create an instance of an object.
rect = Rectangle()
# Use setters methods to set values.
rect.set_x(100)
rect.set_y(100)
rect.set_width(200)
rect.set_height(100)
rect.set_color("blue")
# Use draw method to draw.
rect.draw()

# Create an instance of an object.
oval = Oval()
# Call randomize method choose a value for each attributes.
oval.randomize()
# Use draw method to draw.
oval.draw()

# Create an instance of an object.
tri = Triangle(5, 5, 100, 5, 100, 200)
# Use draw method to draw.
tri.draw()

# Use display method of the Paper object.
paper.display()